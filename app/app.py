from flask import Flask, render_template
import random

app = Flask(__name__)

quotes = [
    ("Courage is not the absence of fear, but the triumph over it.", "Nelson Mandela"),
    ("Do what you can, with what you have, where you are.", "Theodore Roosevelt"),
    ("The journey of a thousand miles begins with one step.", "Lao Tzu"),
    ("Small deeds done are better than great deeds planned.", "Peter Marshall"),
    ("It always seems impossible until it's done.", "Nelson Mandela"),
    ("What you do today can improve all your tomorrows.", "Ralph Marston"),
    ("Act as if it were impossible to fail.", "Dorothy Broude"),
    ("Never bend your head. Always hold it high.", "Helen Keller"),
    ("You must do the things you think you cannot do.", "Eleanor Roosevelt"),
    ("The harder the conflict, the greater the triumph.", "George Washington"),
    ("Success usually comes to those who are too busy to be looking for it.", "Henry David Thoreau"),
    ("Don’t count the days, make the days count.", "Muhammad Ali"),
    ("It does not matter how slowly you go as long as you do not stop.", "Confucius"),
    ("Fall seven times and stand up eight.", "Japanese Proverb"),
    ("Inhale confidence, exhale doubt.", "Unknown"),
    ("The best revenge is massive success.", "Frank Sinatra"),
    ("Be so good they can't ignore you.", "Steve Martin"),
    ("What we achieve inwardly will change outer reality.", "Plutarch"),
    ("He who is not courageous enough to take risks will accomplish nothing in life.", "Muhammad Ali"),
    ("The best way to predict the future is to create it.", "Peter Drucker"),
    ("Do not wait; the time will never be 'just right.'", "Napoleon Hill"),
    ("With the new day comes new strength and new thoughts.", "Eleanor Roosevelt"),
    ("Your life does not get better by chance, it gets better by change.", "Jim Rohn"),
    ("Everything you can imagine is real.", "Pablo Picasso"),
    ("Your limitation—it’s only your imagination.", "Unknown"),
    ("Push yourself, because no one else is going to do it for you.", "Unknown"),
    ("Great things never come from comfort zones.", "Unknown"),
    ("Dream it. Wish it. Do it.", "Unknown"),
    ("Stay positive, work hard, make it happen.", "Unknown"),
    ("Sometimes later becomes never. Do it now.", "Unknown"),
    ("Don’t wait for opportunity. Create it.", "Unknown"),
    ("The key to success is to focus on goals, not obstacles.", "Unknown"),
    ("Don't watch the clock; do what it does. Keep going.", "Sam Levenson"),
    ("Keep your face always toward the sunshine—and shadows will fall behind you.", "Walt Whitman"),
    ("Opportunities don't happen. You create them.", "Chris Grosser"),
    ("Success is not how high you have climbed, but how you make a positive difference to the world.", "Roy T. Bennett"),
    ("You are braver than you believe, stronger than you seem, and smarter than you think.", "A.A. Milne"),
    ("The only limit to our realization of tomorrow will be our doubts of today.", "Franklin D. Roosevelt"),
    ("If you can dream it, you can do it.", "Walt Disney"),
    ("Don’t wait for the perfect moment. Take the moment and make it perfect.", "Zoey Sayward"),
    ("Life is 10% what happens to us and 90% how we react to it.", "Charles R. Swindoll"),
    ("The difference between ordinary and extraordinary is that little extra.", "Jimmy Johnson"),
    ("Motivation is what gets you started. Habit is what keeps you going.", "Jim Ryun"),
    ("Failure will never overtake me if my determination to succeed is strong enough.", "Og Mandino"),
    ("Start where you are. Use what you have. Do what you can.", "Arthur Ashe"),
    ("Success is liking yourself, liking what you do, and liking how you do it.", "Maya Angelou"),
    ("You don’t have to be great to start, but you have to start to be great.", "Zig Ziglar"),
    ("Do not fear mistakes. You will know failure. Continue to reach out.", "Benjamin Franklin"),
    ("Great minds discuss ideas; average minds discuss events; small minds discuss people.", "Eleanor Roosevelt"),
    ("A champion is defined not by their wins but by how they can recover when they fall.", "Serena Williams"),
    ("The best preparation for tomorrow is doing your best today.", "H. Jackson Brown Jr."),
    ("Perseverance is not a long race; it is many short races one after the other.", "Walter Elliot"),
    ("If opportunity doesn’t knock, build a door.", "Milton Berle"),
    ("Don’t let what you cannot do interfere with what you can do.", "John Wooden"),
    ("Everything has beauty, but not everyone sees it.", "Confucius"),
    ("The mind is everything. What you think you become.", "Buddha"),
    ("Success is how high you bounce when you hit bottom.", "George S. Patton"),
    ("Believe in yourself and all that you are.", "Christian D. Larson"),
    ("Work hard in silence, let success make the noise.", "Frank Ocean"),
    ("Don’t be pushed around by the fears in your mind. Be led by the dreams in your heart.", "Roy T. Bennett"),
    ("The secret to success is to know something nobody else knows.", "Aristotle Onassis"),
    ("Success is the sum of small efforts, repeated day-in and day-out.", "Robert Collier"),
    ("The way to get started is to quit talking and begin doing.", "Walt Disney"),
    ("A year from now you may wish you had started today.", "Karen Lamb"),
    ("Do not go where the path may lead, go instead where there is no path and leave a trail.", "Ralph Waldo Emerson")
]


@app.route('/')
def home():
    quote = random.choice(quotes)
    return render_template('index.html', quote=quote)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
