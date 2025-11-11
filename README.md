# AI_Based_Syatem
School project
1. Weather Outfit Helper

	What it does: Suggests what to wear based on the weather.

	How it works using rules: If it's cold, suggest a jacket. If it's hot, suggest shorts. Rules like if temperature < 50 then wear jacket.

2. Basic Math Tutor

 	What it does: Helps users solve simple math problems like addition or multiplication.

	How it works using rules: Matches keywords like “add” or “multiply” and applies rules like if input includes 'add' then add the numbers.

3. Simple Meal Planner

	What it does: Recommends meals based on time of day.

	How it works using rules: Uses rules like if thime  morning then suggest breakfast or if time == evening then suggest dinner.

I like this idea because it's easy to understand and fun to build. It shows how simple rules can lead to useful suggestions, and it’s a great way to learn how rule based systems respond to changing inputs.



🧥 Weather Outfit Helper – Rule-Based Logic

Goal: Suggest clothing based on temperature and weather conditions.

🔧 Rules (IF-THEN format)

1. 	Temperature-Based Rules

• 	IF temperature < 40°F THEN suggest "heavy coat, gloves, and hat"

• 	IF temperature ≥ 40°F AND < 60°F THEN suggest "jacket or sweater"

• 	IF temperature ≥ 60°F AND < 75°F THEN suggest "long sleeves or light layers"

• 	IF temperature ≥ 75°F THEN suggest "shorts and t-shirt"

2. 	Weather Condition Rules

• 	IF condition == "rain" THEN suggest "umbrella and waterproof jacket"

• 	IF condition == "snow" THEN suggest "boots and insulated coat"

• 	IF condition == "sunny" THEN suggest "sunglasses and sunscreen"

• 	IF condition == "windy" THEN suggest "windbreaker or scarf"

3. 	Combined Rules

• 	IF temperature < 40°F AND condition == "snow" THEN suggest "heavy coat, boots, gloves, and hat"

• 	IF temperature ≥ 75°F AND condition == "sunny" THEN suggest "shorts, t-shirt, sunglasses, and sunscreen"
