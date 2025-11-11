# Weather Outfit Helper - Usage Guide

## 🌡️ Overview
The Weather Outfit Helper is a rule-based AI system that suggests appropriate clothing based on current temperature and weather conditions. This demonstrates how simple IF-THEN rules can create useful, intelligent behavior.

## 🚀 Getting Started

### Running the Interactive System
```powershell
python weather_outfit_helper.py
```

This launches an interactive menu where you can:
1. Get outfit suggestions by entering temperature and weather conditions
2. View all the rules used by the system
3. Exit the program

### Running the Test Suite
```powershell
python test_weather_system.py
```

This runs automated tests to verify the system works correctly across various scenarios.

## 📋 System Rules

### Temperature-Based Rules
- **IF** temperature < 40°F **THEN** suggest "heavy coat, gloves, and hat"
- **IF** temperature ≥ 40°F AND < 60°F **THEN** suggest "jacket or sweater"
- **IF** temperature ≥ 60°F AND < 75°F **THEN** suggest "long sleeves or light layers"
- **IF** temperature ≥ 75°F **THEN** suggest "shorts and t-shirt"

### Weather Condition Rules
- **IF** condition == "rain" **THEN** suggest "umbrella and waterproof jacket"
- **IF** condition == "snow" **THEN** suggest "boots and insulated coat"
- **IF** condition == "sunny" **THEN** suggest "sunglasses and sunscreen"
- **IF** condition == "windy" **THEN** suggest "windbreaker or scarf"

### Combined Rules (Higher Priority)
- **IF** temperature < 40°F AND condition == "snow" **THEN** suggest "heavy coat, boots, gloves, and hat"
- **IF** temperature ≥ 75°F AND condition == "sunny" **THEN** suggest "shorts, t-shirt, sunglasses, and sunscreen"

## 💡 Examples

### Example 1: Cold and Snowy
```
Input: Temperature = 35°F, Condition = snow
Output: Wear heavy coat, boots, gloves, and hat
```

### Example 2: Hot and Sunny
```
Input: Temperature = 85°F, Condition = sunny
Output: Wear shorts, t-shirt, sunglasses, and sunscreen
```

### Example 3: Cool and Rainy
```
Input: Temperature = 50°F, Condition = rain
Output: Wear jacket or sweater, umbrella and waterproof jacket
```

## 🔧 Using the System Programmatically

```python
from weather_outfit_helper import WeatherOutfitHelper

# Create an instance
helper = WeatherOutfitHelper()

# Get a suggestion
suggestion = helper.suggest_outfit(temperature=65, condition="sunny")
print(suggestion)

# View the rules
rules = helper.explain_rules()
print(rules)
```

## 📚 System Architecture

### Class: `WeatherOutfitHelper`

**Methods:**
- `get_temperature_suggestion(temperature)` - Applies temperature-based rules
- `get_condition_suggestion(condition)` - Applies weather condition rules
- `get_combined_suggestion(temperature, condition)` - Applies combined rules
- `suggest_outfit(temperature, condition)` - Main method that returns outfit suggestion
- `explain_rules()` - Returns formatted string of all rules

### Rule Priority
1. **Combined rules** are checked first (most specific)
2. **Temperature rules** are applied next
3. **Condition rules** are added to the suggestion
4. All applicable suggestions are combined

## 🎓 Educational Value

This project demonstrates:
- **Rule-Based AI**: How IF-THEN rules create intelligent behavior
- **Expert Systems**: Encoding human knowledge into computational rules
- **Logic Programming**: Using conditional logic to make decisions
- **Modular Design**: Separating different rule types into methods
- **User Interaction**: Creating an intuitive interface for AI systems

## 🛠️ Requirements
- Python 3.6 or higher
- No external dependencies required (uses only standard library)

## 📝 Project Structure
```
AI_Based_Syatem/
├── weather_outfit_helper.py    # Main system implementation
├── test_weather_system.py      # Automated test suite
├── USAGE.md                    # This file
└── README.md                   # Project description
```

## 🤝 Future Enhancements
Possible improvements to explore:
- Add humidity-based rules
- Include time-of-day considerations
- Add seasonal adjustments
- Support for multiple temperature units (Celsius/Fahrenheit)
- Include activity-based suggestions (work, sports, formal events)
- Add fuzzy logic for temperature transitions
