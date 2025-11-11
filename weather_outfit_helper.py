"""
Weather Outfit Helper - Rule-Based AI System
A simple AI system that suggests clothing based on temperature and weather conditions.
"""

class WeatherOutfitHelper:
    """Rule-based system for suggesting outfits based on weather conditions."""
    
    def __init__(self):
        self.suggestions = []
    
    def get_temperature_suggestion(self, temperature):
        """Apply temperature-based rules to suggest clothing."""
        if temperature < 40:
            return "heavy coat, gloves, and hat"
        elif 40 <= temperature < 60:
            return "jacket or sweater"
        elif 60 <= temperature < 75:
            return "long sleeves or light layers"
        else:  # temperature >= 75
            return "shorts and t-shirt"
    
    def get_condition_suggestion(self, condition):
        """Apply weather condition rules to suggest accessories."""
        condition = condition.lower()
        
        if condition == "rain":
            return "umbrella and waterproof jacket"
        elif condition == "snow":
            return "boots and insulated coat"
        elif condition == "sunny":
            return "sunglasses and sunscreen"
        elif condition == "windy":
            return "windbreaker or scarf"
        else:
            return None
    
    def get_combined_suggestion(self, temperature, condition):
        """Apply combined rules for specific temperature and condition combinations."""
        condition = condition.lower()
        
        # Combined rule: Cold and snowy
        if temperature < 40 and condition == "snow":
            return "heavy coat, boots, gloves, and hat"
        
        # Combined rule: Hot and sunny
        elif temperature >= 75 and condition == "sunny":
            return "shorts, t-shirt, sunglasses, and sunscreen"
        
        return None
    
    def suggest_outfit(self, temperature, condition="clear"):
        """
        Main method to suggest outfit based on temperature and weather condition.
        
        Args:
            temperature (float): Temperature in Fahrenheit
            condition (str): Weather condition (rain, snow, sunny, windy, clear)
        
        Returns:
            str: Outfit suggestion
        """
        self.suggestions = []
        
        # Check for combined rules first (more specific)
        combined = self.get_combined_suggestion(temperature, condition)
        if combined:
            return f"🧥 Outfit Suggestion:\n   Wear: {combined}"
        
        # Apply temperature-based rule
        temp_suggestion = self.get_temperature_suggestion(temperature)
        self.suggestions.append(temp_suggestion)
        
        # Apply condition-based rule
        condition_suggestion = self.get_condition_suggestion(condition)
        if condition_suggestion:
            self.suggestions.append(condition_suggestion)
        
        # Combine all suggestions
        outfit = ", ".join(self.suggestions)
        return f"🧥 Outfit Suggestion:\n   Wear: {outfit}"
    
    def explain_rules(self):
        """Display the rules used by the system."""
        rules = """
        ╔══════════════════════════════════════════════════════════════╗
        ║           WEATHER OUTFIT HELPER - RULE SYSTEM                ║
        ╚══════════════════════════════════════════════════════════════╝
        
        📋 TEMPERATURE-BASED RULES:
        • IF temperature < 40°F THEN suggest "heavy coat, gloves, and hat"
        • IF temperature ≥ 40°F AND < 60°F THEN suggest "jacket or sweater"
        • IF temperature ≥ 60°F AND < 75°F THEN suggest "long sleeves or light layers"
        • IF temperature ≥ 75°F THEN suggest "shorts and t-shirt"
        
        🌦️  WEATHER CONDITION RULES:
        • IF condition == "rain" THEN suggest "umbrella and waterproof jacket"
        • IF condition == "snow" THEN suggest "boots and insulated coat"
        • IF condition == "sunny" THEN suggest "sunglasses and sunscreen"
        • IF condition == "windy" THEN suggest "windbreaker or scarf"
        
        🔄 COMBINED RULES:
        • IF temperature < 40°F AND condition == "snow" 
          THEN suggest "heavy coat, boots, gloves, and hat"
        • IF temperature ≥ 75°F AND condition == "sunny" 
          THEN suggest "shorts, t-shirt, sunglasses, and sunscreen"
        """
        return rules


def main():
    """Main function to run the Weather Outfit Helper."""
    helper = WeatherOutfitHelper()
    
    print("=" * 65)
    print("       🌡️  WEATHER OUTFIT HELPER - AI Rule-Based System")
    print("=" * 65)
    print()
    
    while True:
        print("\nOptions:")
        print("  1. Get outfit suggestion")
        print("  2. View system rules")
        print("  3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == "1":
            try:
                # Get temperature input
                temp_input = input("\n🌡️  Enter temperature (°F): ").strip()
                temperature = float(temp_input)
                
                # Get weather condition input
                print("\n🌦️  Weather conditions: rain, snow, sunny, windy, clear")
                condition = input("   Enter weather condition: ").strip()
                
                # Get suggestion
                suggestion = helper.suggest_outfit(temperature, condition)
                print("\n" + "─" * 65)
                print(suggestion)
                print("─" * 65)
                
            except ValueError:
                print("\n❌ Error: Please enter a valid number for temperature.")
            except Exception as e:
                print(f"\n❌ Error: {e}")
        
        elif choice == "2":
            print(helper.explain_rules())
        
        elif choice == "3":
            print("\n👋 Thank you for using Weather Outfit Helper!")
            break
        
        else:
            print("\n❌ Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
