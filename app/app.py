from flask import Flask, render_template
import random

app = Flask(__name__)

quotes = [
    ("The best way to get started is to quit talking and begin doing.", "Walt Disney"),
    ("Don't let yesterday take up too much of today.", "Will Rogers"),
    ("It's not whether you get knocked down, it's whether you get up.", "Vince Lombardi"),
    ("If you are working on something exciting, it will keep you motivated.", "Steve Jobs"),
    ("Success is not in what you have, but who you are.", "Bo Bennett"),
    ("Hardships often prepare ordinary people for an extraordinary destiny.", "C.S. Lewis"),
    ("The only way to do great work is to love what you do.", "Steve Jobs"),
    ("Believe you can and you're halfway there.", "Theodore Roosevelt"),
    ("Success is not final, failure is not fatal: It is the courage to continue that counts.", "Winston Churchill"),
    ("You miss 100% of the shots you don’t take.", "Wayne Gretzky"),
    ("In the middle of every difficulty lies opportunity.", "Albert Einstein"),
    ("Don’t watch the clock; do what it does. Keep going.", "Sam Levenson"),
    ("You are never too old to set another goal or to dream a new dream.", "C.S. Lewis"),
    ("Success is walking from failure to failure with no loss of enthusiasm.", "Winston Churchill"),
    ("Success is not the key to happiness. Happiness is the key to success.", "Albert Schweitzer"),
    ("Do not wait to strike till the iron is hot, but make it hot by striking.", "William Butler Yeats"),
    ("What you get by achieving your goals is not as important as what you become by achieving your goals.", "Zig Ziglar"),
    ("To live is the rarest thing in the world. Most people exist, that is all.", "Oscar Wilde"),
    ("That it will never come again is what makes life so sweet.", "Emily Dickinson"),
    ("It is never too late to be what you might have been.", "George Eliot"),
    ("To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment.", "Ralph Waldo Emerson"),
    ("Pain is inevitable. Suffering is optional.", "Haruki Murakami"),
    ("All the world's a stage, and all the men and women merely players.", "William Shakespeare"),
    ("Be kind, for everyone you meet is fighting a hard battle.", "Plato"),
    ("Don’t let your happiness depend on something you may lose.", "C.S. Lewis"),
    ("We are all broken, that's how the light gets in.", "Ernest Hemingway"),
    ("Appreciation is a wonderful thing. It makes what is excellent in others belong to us as well.", "Voltaire"),
    ("Life is tough my darling, but so are you.", "Stephanie Bennett Henry"),
    ("Self-awareness and self-love matter. Who we are is how we lead.", "Brené Brown"),
    ("Amateurs sit and wait for inspiration, the rest of us just get up and go to work.", "Stephen King"),
    ("There is some good in this world, and it’s worth fighting for.", "J.R.R. Tolkien"),
    ("Beware; for I am fearless, and therefore powerful.", "Mary Shelley"),
    ("The only way out of the labyrinth of suffering is to forgive.", "John Green"),
    ("I am not afraid of storms, for I am learning how to sail my ship.", "Louisa May Alcott"),
    ("Our greatest glory is not in never falling, but in rising every time we fall.", "Confucius"),
    ("Life is to be lived, not controlled; and humanity is won by continuing to play in face of certain defeat.", "Ralph Ellison"),
    ("If a story is in you, it has to come out.", "William Faulkner"),
    ("A word after a word after a word is power.", "Margaret Atwood"),
    ("Your intuition knows what to write, so get out of the way.", "Ray Bradbury"),
    ("The scariest moment is always just before you start.", "Stephen King"),
    ("Fill your paper with the breathings of your heart.", "William Wordsworth"),
    ("Good stories are not written. They are rewritten.", "Phyllis Whitney"),
    ("The secret of getting ahead is getting started.", "Mark Twain"),
    ("As a writer, you should not judge. You should understand.", "Ernest Hemingway"),
    ("The most valuable of all talents is that of never using two words when one will do.", "Thomas Jefferson"),
    ("Writers live twice.", "Natalie Goldberg"),
    ("To produce a mighty book, you must choose a mighty theme.", "Herman Melville"),
    ("Get it down. Take chances. It may be bad, but it’s the only way you can do anything really good.", "William Faulkner"),
    ("The secret of it all is to write… without waiting for a fit time or place.", "Walt Whitman"),
    ("Every sunrise is a message from God, and every sunset is his signature.", "William Arthur Ward"),
    ("If you can imagine it, you can achieve it; if you can dream it, you can become it.", "William Arthur Ward"),
    ("Alter your attitude and you will change your life.", "William Arthur Ward"),
    ("The mediocre teacher tells. The good teacher explains. The superior teacher demonstrates. The great teacher inspires.", "William Arthur Ward"),
    ("No person is strong enough to carry a cross and a prejudice at the same time.", "William Arthur Ward"),
    ("Dream big and dare to fail.", "Norman Vaughan"),
    ("What lies behind us and what lies before us are tiny matters compared to what lies within us.", "Ralph Waldo Emerson"),
    ("Doubt kills more dreams than failure ever will.", "Suzy Kassem"),
    ("Act as if what you do makes a difference. It does.", "William James"),
    ("Everything you’ve ever wanted is on the other side of fear.", "George Addair"),
    ("Go confidently in the direction of your dreams. Live the life you have imagined.", "Henry David Thoreau"),
    ("Limit your 'always' and your 'nevers'.", "Amy Poehler"),
    ("Nothing will work unless you do.", "Maya Angelou"),
    ("Try to be a rainbow in someone else's cloud.", "Maya Angelou"),
    ("You do not find the happy life. You make it.", "Camilla Eyring Kimball"),
    ("Happiness often sneaks in through a door you didn’t know you left open.", "John Barrymore"),
    ("Happiness is not something ready made. It comes from your own actions.", "Dalai Lama"),
    ("Impossible is just an opinion.", "Paulo Coelho"),
    ("Magic is believing in yourself. If you can do that, you can make anything happen.", "Johann Wolfgang von Goethe"),
    ("Stay away from those people who try to disparage your ambitions.", "Mark Twain")
]


@app.route('/')
def home():
    quote = random.choice(quotes)
    return render_template('index.html', quote=quote)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
