import os
import datetime

# Helper to ensure directory exists
def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

books = [
    {
        "id": 1,
        "title": "How To Be Late Even When You Start Early",
        "slug": "how-to-be-late-even-when-you-start-early",
        "ebook": "https://www.amazon.com/dp/B0GGFFZBY4",
        "paperback": "https://www.amazon.com/dp/B0GGHC6T67",
        "cover": "https://m.media-amazon.com/images/I/91HiLxrp-XL._SL1500_.jpg",
        "catchphrase": "The definitive parody self-help guide for the chronically late.",
        "topic": "Time Blindness & Lateness",
        "desc_base": "Ever started getting ready two hours early only to end up ten minutes late? Welcome to the definitive parody self-help guide for the chronically late.",
        "theme": "time_management"
    },
    {
        "id": 2,
        "title": "How To Be Exhausted By Decisions That Don't Matter",
        "slug": "how-to-be-exhausted-by-decisions-that-dont-matter",
        "ebook": "https://www.amazon.com/dp/B0GGDN7PR5",
        "paperback": "https://www.amazon.com/dp/B0GGHD1K34",
        "cover": "https://m.media-amazon.com/images/I/9179uhuLOFL._SL1500_.jpg",
        "catchphrase": "Paralyzed by what brand of toothpaste to buy? This is your manifesto.",
        "topic": "Decision Fatigue & Overthinking",
        "desc_base": "Paralyzed by what brand of toothpaste to buy? Exhausted by the 4:00 PM 'what's for dinner' crisis? Finally, a parody self-help guide that understands your struggle.",
        "theme": "decision_making"
    },
    {
        "id": 3,
        "title": "How To Achieve Burnout Without Achieving Anything",
        "slug": "how-to-achieve-burnout-without-achieving-anything",
        "ebook": "https://www.amazon.com/dp/B0GGFG8HLW",
        "paperback": "https://www.amazon.com/dp/B0GGHRV65J",
        "cover": "https://m.media-amazon.com/images/I/91WigqKWRqL._SL1500_.jpg",
        "catchphrase": "Stop accidentally succeeding and learn to fail with intention.",
        "topic": "Burnout & Hustle Culture",
        "desc_base": "Tired of 'rising and grinding' toward a nervous breakdown? Stop accidentally succeeding and learn to fail with intention.",
        "theme": "burnout"
    },
    {
        "id": 4,
        "title": "Why Everyone Is Wrong Except Me: A Scientific Study",
        "slug": "why-everyone-is-wrong-except-me",
        "ebook": "https://www.amazon.com/dp/B0GF6JGWPZ",
        "paperback": "https://www.amazon.com/dp/B0GFMCFH5D",
        "cover": "https://m.media-amazon.com/images/I/91FHiKJgScL._SL1500_.jpg",
        "catchphrase": "Because evidence is optional — confidence is not.",
        "topic": "Ego & Being Right",
        "desc_base": "Have you ever felt that everyone is wrong except you? Science agrees. This is a razor-sharp self-help satire that boldly presents facts that prove you’re right.",
        "theme": "ego"
    },
    {
        "id": 5,
        "title": "Why Success Feels Illegal To Me",
        "slug": "why-success-feels-illegal-to-me",
        "ebook": "https://www.amazon.com/dp/B0GF6RKLKG",
        "paperback": "https://www.amazon.com/dp/B0GFMDDNK4",
        "cover": "https://m.media-amazon.com/images/I/91IW1g2bjQL._SL1500_.jpg",
        "catchphrase": "Sometimes success isn’t scary — believing you earned it is.",
        "topic": "Imposter Syndrome",
        "desc_base": "Ever feel like success feels illegal—like you’re about to be caught for winning? A sharp self-help satire that dives into success guilt.",
        "theme": "imposter_syndrome"
    },
    {
        "id": 6,
        "title": "Why Do I Hate Everyone Before Coffee",
        "slug": "why-do-i-hate-everyone-before-coffee",
        "ebook": "https://www.amazon.com/dp/B0GF6F8B7W",
        "paperback": "https://www.amazon.com/dp/B0GF8DKCHM",
        "cover": "https://m.media-amazon.com/images/I/91V1eWVBVwL._SL1500_.jpg",
        "catchphrase": "Coffee first. Humanity later.",
        "topic": "Coffee Addiction & Morning Rage",
        "desc_base": "Do you hate everyone before coffee? You’re not alone. A hilarious self-help satire that finally explains morning rage.",
        "theme": "coffee"
    },
    {
        "id": 7,
        "title": "I Promise I’ll Start Tomorrow, A Procrastinator’s Notebook",
        "slug": "i-promise-ill-start-tomorrow",
        "ebook": "https://www.amazon.com/dp/B0GF6FYWVZ",
        "paperback": "https://www.amazon.com/dp/B0GF6FYWVZ",
        "cover": "https://m.media-amazon.com/images/I/71jaxaBc0HL._SL1499_.jpg",
        "catchphrase": "The comedy journal you didn’t know you needed—but will absolutely use to avoid doing something important.",
        "topic": "Procrastination",
        "desc_base": "Are you a professional procrastinator? Then this is your new favorite notebook. A hilarious collection of relatable procrastination stories.",
        "theme": "procrastination"
    },
    {
        "id": 8,
        "title": "Why Am I Tired After Doing Nothing All Day",
        "slug": "why-am-i-tired-after-doing-nothing-all-day",
        "ebook": "https://www.amazon.com/dp/B0GDS3FJ2W",
        "paperback": "https://www.amazon.com/dp/B0GF1M19H9",
        "cover": "https://m.media-amazon.com/images/I/91tHS6muSQL._SL1500_.jpg",
        "catchphrase": "Because being exhausted doesn’t always mean you’ve been busy.",
        "topic": "Chronic Fatigue & Laziness",
        "desc_base": "Ever wonder why you’re tired after doing nothing all day? A hilarious self-help satire for anyone trapped in modern adulting burnout.",
        "theme": "tiredness"
    },
    {
        "id": 9,
        "title": "I'm Not Lazy I'm On Energy Saving Mode",
        "slug": "im-not-lazy-im-on-energy-saving-mode",
        "ebook": "https://www.amazon.com/dp/B0GDZ5QS2S",
        "paperback": "https://www.amazon.com/dp/B0GF1KCVYM",
        "cover": "https://m.media-amazon.com/images/I/91XlR1IxWAL._SL1500_.jpg",
        "catchphrase": "Because who says you can’t be lazy but winning?",
        "topic": "Productivity Satire",
        "desc_base": "Tired of being told to “hustle harder”? The ultimate productivity satire for anyone who knows that productivity is overrated.",
        "theme": "laziness"
    },
    {
        "id": 10,
        "title": "I Have No Idea What I am Doing But It's Working",
        "slug": "i-have-no-idea-what-i-am-doing-but-its-working",
        "ebook": "https://www.amazon.com/dp/B0GDZHZRRB",
        "paperback": "https://www.amazon.com/dp/B0GF1XRRC9",
        "cover": "https://m.media-amazon.com/images/I/91mdheGdhSL._SL1500_.jpg",
        "catchphrase": "Success doesn’t always come from knowing what you’re doing.",
        "topic": "Faking Success",
        "desc_base": "Ever wondered how people succeed without a plan? The hilarious self-help parody for anyone clueless but successful.",
        "theme": "success"
    },
    {
        "id": 11,
        "title": "How To Ruin Your Life With One Bad Decision",
        "slug": "how-to-ruin-your-life-with-one-bad-decision",
        "ebook": "https://www.amazon.com/dp/B0GDMCZKNM",
        "paperback": "https://www.amazon.com/dp/B0GDVJMK4F",
        "cover": "https://m.media-amazon.com/images/I/910TsYMGVYL._SL1500_.jpg",
        "catchphrase": "Confidence in bad decisions is easy—living with the consequences is not.",
        "topic": "Bad Decisions & Regret",
        "desc_base": "Ever wondered how to ruin your life with one bad decision? This brutally honest self-help satire explores the life-ruining mistakes.",
        "theme": "regret"
    },
    {
        "id": 12,
        "title": "How To Be Productive Without Producing Anything",
        "slug": "how-to-be-productive-without-producing-anything",
        "ebook": "https://www.amazon.com/dp/B0GDTYVQC9",
        "paperback": "https://www.amazon.com/dp/B0GDVFT5VL",
        "cover": "https://m.media-amazon.com/images/I/91o3z8RJ5TL._SL1500_.jpg",
        "catchphrase": "Results are optional—but looking productive is mandatory.",
        "topic": "Fake Productivity",
        "desc_base": "Tired of working nonstop and still getting nothing done? A sharp productivity satire that exposes the art of fake productivity.",
        "theme": "fake_work"
    },
    {
        "id": 13,
        "title": "How To Be Broke With Confidence",
        "slug": "how-to-be-broke-with-confidence",
        "ebook": "https://www.amazon.com/dp/B0GDTXSTZM",
        "paperback": "https://www.amazon.com/dp/B0GDVG5K5F",
        "cover": "https://m.media-amazon.com/images/I/91q6nJuywkL._SL1500_.jpg",
        "catchphrase": "When the bank account is empty, confidence is the only currency left.",
        "topic": "Financial Satire",
        "desc_base": "Ever wondered how to stay broke forever—and somehow feel amazing about it? The ultimate satire self-help book for financial disasters.",
        "theme": "money"
    },
    {
        "id": 14,
        "title": "How To Politely Tell Someone That You Don't Like Them",
        "slug": "how-to-politely-tell-someone-that-you-dont-like-them",
        "ebook": "https://www.amazon.com/dp/B0G48PMFW5",
        "paperback": "https://www.amazon.com/dp/B0G498TRYM",
        "cover": "https://m.media-amazon.com/images/I/71-tFh9st8L._SL1500_.jpg",
        "catchphrase": "Sometimes the politest thing you can do is tell the truth — with a smile.",
        "topic": "Social Awkwardness & Rejection",
        "desc_base": "A hilariously honest collection of comedic stories and satirical life lessons for anyone who’s ever dealt with an annoying coworker.",
        "theme": "social"
    },
    {
        "id": 15,
        "title": "How Can You Face Your Problem When the Problem Is Your Face ?",
        "slug": "how-can-you-face-your-problem-when-the-problem-is-your-face",
        "ebook": "https://www.amazon.com/dp/B0G46PP4M8",
        "paperback": "https://www.amazon.com/dp/B0G48G79TJ",
        "cover": "https://m.media-amazon.com/images/I/71NDLPEIUCL._SL1500_.jpg",
        "catchphrase": "If you’ve ever looked in the mirror and thought, 'Wow… yikes,' this book is for you.",
        "topic": "Self-Esteem Satire",
        "desc_base": "A hilarious collection of satire and painfully relatable stories about the everyday disasters we all pretend we’re too mature to still experience.",
        "theme": "self_image"
    },
    {
        "id": 16,
        "title": "How Can I Double My Body Fat And Give It To The Next Person",
        "slug": "how-can-i-double-my-body-fat-and-give-it-to-the-next-person",
        "ebook": "https://www.amazon.com/dp/B0G431NM82",
        "paperback": "https://www.amazon.com/dp/B0G44C5BLN",
        "cover": "https://m.media-amazon.com/images/I/711nFogc2pL._SL1500_.jpg",
        "catchphrase": "Enjoy the chaos of fitness clickbait madness.",
        "topic": "Diet & Fitness Satire",
        "desc_base": "A wildly absurd, laugh-out-loud collection of satirical stories that poke fun at self-help culture and miracle fitness hacks.",
        "theme": "fitness"
    },
    {
        "id": 17,
        "title": "How To Hold In Your Fart When Talking To Your Crush",
        "slug": "how-to-hold-in-your-fart-when-talking-to-your-crush",
        "ebook": "https://www.amazon.com/dp/B0G42G92X9",
        "paperback": "https://www.amazon.com/dp/B0G446WJJ9",
        "cover": "https://m.media-amazon.com/images/I/81z4n4qYxQL._SL1500_.jpg",
        "catchphrase": "Get ready to laugh, wince, and say, 'Yep… been there.'",
        "topic": "Dating Disasters",
        "desc_base": "A hilarious collection of awkward, relatable, and absolutely ridiculous stories about the moments we all pretend never happened.",
        "theme": "dating"
    },
    {
        "id": 18,
        "title": "How To Fart And Blame It On Someone: A Gaslighting Guide",
        "slug": "how-to-fart-and-blame-it-on-someone",
        "ebook": "https://www.amazon.com/dp/B0FVX8NVVS",
        "paperback": "https://www.amazon.com/dp/B0FWCXQB24",
        "cover": "https://m.media-amazon.com/images/I/81SeN2VjMIL._SL1500_.jpg",
        "catchphrase": "Change the way you own the room… or clear it.",
        "topic": "Social Etiquette Satire",
        "desc_base": "Ever been caught in a suspiciously smelly situation? This groundbreaking guide will teach you the ancient art of flatulent misdirection.",
        "theme": "etiquette"
    },
    {
        "id": 19,
        "title": "HOW TO DODGE THE BARBER’S SAUSAGE WHILE GETTING A HAIRCUT",
        "slug": "how-to-dodge-the-barbers-sausage",
        "ebook": "https://www.amazon.com/dp/B0FP8WBKQH",
        "paperback": "https://www.amazon.com/dp/B0FP4R7MCZ",
        "cover": "https://m.media-amazon.com/images/I/81aaZf3oKWL._SL1500_.jpg",
        "catchphrase": "Emerging unscathed with a fresh cut and your dignity intact.",
        "topic": "Awkward Encounters",
        "desc_base": "A wild ride through the treacherous world of barber chairs and rogue sausages. A tongue-in-cheek survival manual for awkward trims.",
        "theme": "awkward"
    }
]

def generate_book_markdown(book):
    content = f"""---
title: "{book['title']}"
slug: "{book['slug']}"
date: {datetime.date.today()}
draft: false

# Book Details
tagline: "{book['catchphrase']}"
shortDescription: "{book['desc_base']}"
coverImage: "{book['cover']}"
ogImage: "{book['cover']}"

# Pricing & Links
kindlePrice: "9.99"
paperbackPrice: "14.99"
amazonKindle: "{book['ebook']}"
amazonPaperback: "{book['paperback']}"

# Book Metadata
pages: 150
genre: "Satire / Humor"
rating: "4.8"
ratingCount: 520
---

## Are You Ready to Laugh at Your Own Misery?

{book['desc_base']}

In a world obsessed with perfection, high achievement, and maintaining a curated Instagram feed, **{book['title']}** comes as a breath of fresh air (or a sigh of relief). This isn't just a book; it's a mirror reflecting the hilarity of our modern struggles.

### Why You Need This Book

Let's face it: life is absurd. We stress about things that don't matter, we work jobs that drain us for money we spend on therapy to cope with the jobs, and we try to impress people we don't even like. 

Academic Satire dives deep into the **{book['topic']}** with a razor-sharp wit that cuts through the noise of traditional self-help. Instead of telling you to "manifest abundance" or "wake up at 4 AM," this book gives you permission to be human, flawed, and absolutely hilarious.

### What Readers Are Saying

> "I laughed so hard I snorted my coffee. Then I realized I was late for work, which made it even funnier." - *Verified Reader*

> "Finally, a book that understands that my 'energy saving mode' is a lifestyle choice, not a flaw." - *Amazon Reviewer*

### Inside You'll Discover:

*   **The Truth About {book['topic']}:** Why you do it, why it's funny, and why you're not alone.
*   **Satirical Strategies:** "Actionable" advice that is terrible in practice but hilarious in theory.
*   **Relatable Stories:** Moments that will make you say, "Wait, is he spying on me?"
*   **The Ultimate Defense:** How to use humor to deflect judgment from peers, bosses, and judgmental family members.

### Perfect For:

*   Fans of sarcastic humor and dry wit.
*   People who are tired of toxic positivity.
*   Anyone looking for a unique, funny gift for a friend (or a subtle hint).
*   **You**, because you deserve a laugh today.

<div class="book-buttons mt-xl">
  <a href="{book['ebook']}" class="btn btn-yellow btn-lg" target="_blank">Get the eBook</a>
  <a href="{book['paperback']}" class="btn btn-dark btn-lg" target="_blank">Get the Paperback</a>
</div>

---

*Note: This is a work of satire. If you actually follow the advice inside, Academic Satire is not responsible for your inevitable firing, breakup, or general life chaos.*
"""
    return content

def generate_blog_markdown(book):
    # Create SEO-optimized title
    seo_titles = {
        "time_management": "Why You Are Always Late (And Why It's Actually a Superpower)",
        "decision_making": "Analysis Paralysis: Why Picking Dinner Ruins Your Life",
        "burnout": "Quiet Quitting vs. Burnout: The satire Guide to Doing Less",
        "ego": "Why Everyone Else Is Wrong and You Are Right: A Scientific Ego Trip",
        "imposter_syndrome": "Imposter Syndrome or Success Guilt? Why You Feel Like a Fraud",
        "coffee": "Morning Rage is Real: Why People Are Annoying Before Caffeine",
        "procrastination": "The Art of Procrastination: Why Starting Tomorrow is Better",
        "tiredness": "Why Am I So Tired After Doing Absolutely Nothing?",
        "laziness": "Energy Saving Mode: Why Laziness is Just Efficiency in Disguise",
        "success": "Faking Success: How to Wing It Until You Make It",
        "regret": "One Bad Decision: A Guide to Ruining Your Life (Hilariously)",
        "fake_work": "How to Look Busy at Work Without Doing Anything",
        "money": "Broke but Confident: How to Survive Inflation with Swag",
        "social": "How to Politely Tell People You Don't Like Them (Without Getting Slapped)",
        "self_image": "Facing Your Problems When the Problem is Your Face",
        "fitness": "Fitness Satire: Why I Want to Donate My Body Fat",
        "dating": "Dating Nightmares: Holding in Farts and Other Rom-Com Lies",
        "etiquette": "The Gaslighting Guide: How to Blame Your Farts on Others",
        "awkward": "Barber Shop Anxiety: Dodging Sausages and Small Talk"
    }
    
    blog_title = seo_titles.get(book['theme'], f"The Truth About {book['topic']}")
    
    content = f"""---
title: "{blog_title}"
date: {datetime.date.today()}
slug: "{book['slug']}-blog"
categories: ["{book['genre'] if 'genre' in book else 'Satire'}"]
tags: ["{book['theme']}", "humor", "books", "satire"]
summary: "We explore the hilarious reality of {book['topic']} and why {book['title']} is the manual you need right now."
ogImage: "{book['cover']}"
---

Let's be honest. **{book['topic']}** is something we all deal with, but rarely admit to. We live in a society that demands perfection, punctuality, and constant productivity. But what if we leaned into the chaos instead?

## The {book['topic']} Epidemic

It starts small. {book['desc_base']} You tell yourself it's just this once. But soon, it becomes a lifestyle. And you know what? That's okay. Because trying to be perfect is exhausting, and quite frankly, boring.

Imagine a world where we celebrated our flaws instead of hiding them. Where "{book['catchphrase']}" wasn't just a funny saying, but a badge of honor.

## Why Satire is the Best Medicine

When life gets overwhelming, humor is our best defense mechanism. Laughing at our own struggles takes the power away from them. It makes the scary stuff feels managed, and the annoying stuff feel ridiculous.

That's the core philosophy behind my latest book, **[{book['title']}](/books/{book['slug']}/)**.

![{book['title']} Book Cover]({book['cover']})

## A Deep Dive into {book['title']}

This isn't your standard self-help book that tells you to drink more water and journal your feelings (though, hydration is important). This is a **parody guide** designed to make you laugh until your stomach hurts.

In this book, we explore:

1.  **The Absurdity of Modern Life:** Why do we do the things we do?
2.  **Sarcastic Solutions:** Terrible advice that somehow makes sense.
3.  **Relatable Misery:** Knowing that you are not alone in your {book['topic']} struggles.

> "{book['catchphrase']}"

## Why You Should Read It

If you've ever felt seen by a meme, this book is for you. It's affordable, it's funny, and it's cheaper than therapy. Plus, it makes a great gift for that one friend who really needs to hear this message (you know the one).

Stop taking life so seriously. Grab a copy, pour a drink (or coffee), and enjoy the absurdity.

### Get Your Copy Today

**eBook:** [Available on Amazon]({book['ebook']})  
**Paperback:** [Available on Amazon]({book['paperback']})

<div class="text-center mt-xl">
  <a href="/books/{book['slug']}/" class="btn btn-yellow btn-lg">Read More About This Book</a>
</div>
"""
    return content

# Main execution
def main():
    base_path = "/Volumes/Flow/ProfYnot website/content"
    
    for book in books:
        # Generate Book Page
        book_path = f"{base_path}/books/{book['slug']}.md"
        ensure_dir(book_path)
        with open(book_path, "w") as f:
            f.write(generate_book_markdown(book))
        print(f"Created Book: {book['title']}")
        
        # Generate Blog Post
        blog_path = f"{base_path}/blog/{book['slug']}-blog.md"
        ensure_dir(blog_path)
        with open(blog_path, "w") as f:
            f.write(generate_blog_markdown(book))
        print(f"Created Blog: {blog_path}")

if __name__ == "__main__":
    main()
