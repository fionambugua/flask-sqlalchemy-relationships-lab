#!/usr/bin/env python3

from flask import Flask, jsonify, make_response
from flask_migrate import Migrate

from models import db, Event, Session, Speaker, Bio

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

# TODO: add functionality to all routes

@app.route("/events")
def get_events():
    events = [
        {"id": event.id, "name": event.name, "location": event.location}
        for event in Event.query.all()
    ]
    if events:
        return make_response(events, 200)
    return make_response({"message": "No events"}, 404)



@app.route("/events/<int:id>/sessions")
def get_event_sessions(id):
    event = Event.query.filter_by(id=id).first()
    if event:
        sessions = [
            {"id": s.id, "title": s.title, "start_time": s.start_time.isoformat()}
            for s in event.sessions
        ]

        return make_response(sessions, 200)

    return make_response({"error": "Event not found"}, 404)


@app.route("/speakers")
def get_speakers():
    spakers = [
        {"id": speaker.id, "name": speaker.name} for speaker in Speaker.query.all()
    ]
    if spakers:
        return make_response(spakers, 200)

    return make_response({"message": "No speakers"})


@app.route('/speakers/<int:id>')
def get_speaker(id):
    pass


@app.route('/sessions/<int:id>/speakers')
def get_session_speakers(id):
    pass


if __name__ == '__main__':
    app.run(port=5555, debug=True)