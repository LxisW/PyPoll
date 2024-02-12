from flask import Flask, request, jsonify, render_template, redirect, url_for

app = Flask(__name__)
app.debug = True
app.config["env"] = "dev"


@app.route("/", methods=["GET"])
def main_page():
    # start page
    return render_template("index.html")


@app.route("/poll/<poll_id>", methods=["GET"])
def poll_page(poll_id):
    ip = request.remote_addr
    # get poll data
    poll_data = app.db_helper.get_poll_data(poll_id)
    if poll_data != None:
        if poll_data["one_per_ip"]:
            has_voted = app.db_helper.has_voted(ip=ip, poll_id=poll_id)
            # check if user has voted
            if not has_voted:
                return render_template("poll.html", poll_data=poll_data)
            else:
                # if already voted --> redirect to result endpoint"
                return redirect(url_for("result_endpoint", poll_id=poll_id))

        else:
            # multiple votes per IP allowed
            return render_template("poll.html", poll_data=poll_data)

    else:
        return "poll not found"


@app.route("/admin/poll/<poll_id>/settings", methods=["GET"])
def poll_settings(poll_id):
    admin_key = request.args.get("admin_key")
    if admin_key == None:
        return "Please provide an admin key to access this page!"
    # check if admin key is valid and matching the poll id
    valid = app.db_helper.check_admin_key(admin_key=admin_key, poll_id=poll_id)
    if valid:
        # get poll data
        poll_data = app.db_helper.get_poll_data(poll_id=poll_id)
        question = poll_data["question"]
        poll_link = url_for("poll_page", poll_id=poll_id, _external=True)

        return render_template(
            "poll_settings.html",
            question=question,
            admin_key=admin_key,
            poll_id=poll_id,
            poll_link=poll_link,
            headline="Successfully created poll!",
        )

    return "Please enter a valid admin key"


@app.route("/submit", methods=["POST"])
def submit_poll():
    selected_answer = request.form.get("selected_answer")
    poll_id = request.form.get("poll_id")
    ip = request.remote_addr  # only works in production

    if selected_answer:
        print(f"Selected Answer: {selected_answer}")
        one_per_ip = app.db_helper.get_one_per_ip(poll_id=poll_id)
        success = app.db_helper.add_vote(
            poll_id=poll_id, ip=ip, choice=selected_answer, one_per_ip=one_per_ip
        )
        if success:
            # get votes
            return redirect(url_for("result_endpoint", poll_id=poll_id))

        else:
            return "Error submitting poll"
    else:
        print("No answer selected")
        return "Please select an answer", 400


@app.route("/create-poll", methods=["POST"])
def create_poll():
    question = request.form.get("question")
    answer_A = request.form.get("answerA")
    answer_B = request.form.get("answerB")
    answer_C = request.form.get("answerC")
    answer_D = request.form.get("answerD")
    one_per_ip = request.form.get("one_per_ip")
    ip = request.remote_addr

    success, poll_id, admin_key = app.db_helper.create_poll(
        question=question,
        answers={"A": answer_A, "B": answer_B, "C": answer_C, "D": answer_D},
        ip=ip,
        one_per_ip=one_per_ip,
    )
    if success:
        # poll successfully created
        return redirect(url_for("poll_settings", poll_id=poll_id, admin_key=admin_key))
    else:
        # error creating poll
        return "Error creating poll"


@app.route("/results/<poll_id>", methods=["GET"])
def result_endpoint(poll_id):
    ip = request.remote_addr
    has_voted = app.db_helper.has_voted(ip=ip, poll_id=poll_id)
    admin_key = request.args.get("admin_key")
    if admin_key != None:
        valid_admin_key = app.db_helper.check_admin_key(
            admin_key=admin_key, poll_id=poll_id
        )
    else:
        valid_admin_key = False

    if has_voted or valid_admin_key:
        votes = app.db_helper.get_votes(poll_id=poll_id)
        poll_data = app.db_helper.get_poll_data(poll_id=poll_id)
        answers = list(votes.keys())
        temp_answers = []
        for answer in answers:
            temp_answers.append(f"{answer}: {poll_data['answers'][answer]}")
        votes = list(votes.values())
        total_votes = sum(votes)
        question = poll_data["question"]

        data = {
            "a1": answers[0],
            "v1": votes[0],
            "a2": answers[1],
            "v2": votes[1],
            "a3": answers[2],
            "v3": votes[2],
            "a4": answers[3],
            "v4": votes[3],
            "title": question,
            "total_votes": total_votes,
            "wt": 700,
            "ht": 700,
        }

        answers = temp_answers
        return render_template("results.html", **data)
    if poll_id != None:
        return redirect(url_for("poll_page", poll_id=poll_id))
    else:
        return redirect(url_for("main_page"))


# test endpoint to try rendering chart
@app.route("/test", methods=["GET", "POST"])
def get_data__show_chart():
    data = {
        "a1": "Answer 1",
        "v1": 1,
        "a2": "Answer 2",
        "v2": 3,
        "a3": "Answer 3",
        "v3": 2,
        "a4": "Answer 4",
        "v4": 0,
        "title": "Is this the test queston?",
        "total_votes": 6,
        "wt": 700,
        "ht": 700,
    }

    return render_template("results.html", **data)
