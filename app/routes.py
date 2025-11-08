from flask import Flask, request, jsonify, Blueprint, render_template, redirect, url_for, flash
from datetime import datetime
from app import models

# Define a Blueprint (do NOT create a Flask app here)
main = Blueprint('main', __name__)

# UI entry: render the HTML index page (loads when user visits '/')
@main.route('/')
def index():
    workouts = models.get_all_workouts()
    total_time = sum(entry.get('duration', 0) for cat in workouts.values() for entry in cat)
    return render_template('index.html', workouts=workouts, total_time=total_time)

# Summary page (optional separate UI view)
@main.route('/summary')
def summary():
    workouts = models.get_all_workouts()
    total_time = sum(entry.get('duration', 0) for cat in workouts.values() for entry in cat)
    # You can show a more detailed breakdown in summary.html
    return render_template('summary.html', workouts=workouts, total_time=total_time)

# Form POST from the UI to add a workout
@main.route('/add', methods=['POST'])
def add_from_form():
    category = request.form.get('category', 'Workout')
    exercise = (request.form.get('exercise') or '').strip()
    duration = request.form.get('duration', '').strip()

    if not exercise or not duration:
        flash("Please provide both exercise and duration.", "danger")
        return redirect(url_for('.index'))

    try:
        duration_int = int(duration)
    except ValueError:
        flash("Duration must be a number.", "danger")
        return redirect(url_for('.index'))

    try:
        models.add_workout(exercise=exercise, duration=duration_int, category=category)
    except ValueError as e:
        flash(str(e), "danger")
        return redirect(url_for('.index'))

    flash(f"Added {exercise} ({duration_int} min) to {category}.", "success")
    return redirect(url_for('.index'))

# JSON API: get all workouts
@main.route('/api/workouts', methods=['GET'])
def api_get_workouts():
    return jsonify(models.get_all_workouts())

# JSON API: add a workout
@main.route('/api/workouts', methods=['POST'])
def api_add_workout():
    data = request.get_json() or {}
    category = data.get('category', 'Workout')
    exercise = (data.get('exercise') or '').strip()
    duration = data.get('duration')

    if not exercise or duration is None:
        return jsonify(error="Both 'exercise' and 'duration' are required"), 400

    try:
        duration = int(duration)
    except (ValueError, TypeError):
        return jsonify(error="'duration' must be an integer"), 400

    try:
        entry = models.add_workout(exercise=exercise, duration=duration, category=category)
    except ValueError as e:
        return jsonify(error=str(e)), 400

    return jsonify(success=True, entry=entry), 201

# Utility: clear store (useful for development/testing)
@main.route('/clear', methods=['POST'])
def clear_store():
    models.clear_workouts()
    return redirect(url_for('.index'))