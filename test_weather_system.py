"""
Test script for Weather Outfit Helper
Tests various scenarios to verify the rule-based system works correctly.
"""

from weather_outfit_helper import WeatherOutfitHelper

def test_weather_outfit_helper():
    """Test the Weather Outfit Helper with various scenarios."""
    helper = WeatherOutfitHelper()
    
    print("=" * 70)
    print("        TESTING WEATHER OUTFIT HELPER - Rule-Based AI System")
    print("=" * 70)
    print()
    
    # Test scenarios
    test_cases = [
        # (temperature, condition, description)
        (35, "snow", "Very cold and snowy"),
        (45, "rain", "Cool and rainy"),
        (65, "sunny", "Mild and sunny"),
        (80, "sunny", "Hot and sunny"),
        (55, "windy", "Cool and windy"),
        (30, "clear", "Very cold and clear"),
        (78, "clear", "Warm and clear"),
        (50, "rain", "Cool and rainy"),
    ]
    
    print("📋 Running test scenarios...\n")
    
    for i, (temp, condition, description) in enumerate(test_cases, 1):
        print(f"\n{'─' * 70}")
        print(f"Test Case #{i}: {description}")
        print(f"   Temperature: {temp}°F")
        print(f"   Condition: {condition}")
        print(f"{'─' * 70}")
        
        result = helper.suggest_outfit(temp, condition)
        print(result)
    
    print("\n" + "=" * 70)
    print("✅ All test cases completed successfully!")
    print("=" * 70)

if __name__ == "__main__":
    test_weather_outfit_helper()
