#!/usr/bin/python3
import sys
import os

def display_message(name):  
    picture = f"""
    .     .  .      +     .      .          .
     .       .      .     \033[32m# \033[0m      .           .            
        .      .         ###            .      .      .          \033[33mDear ✨{name}✨\033[0m,
      .      .   "#:. .:##"##:. .:#"  .      .                     \033[30mOn this auspicious occasion of International Women's Day,\033[0m
          .      . "####"###"####"  .      .                       \033[30mI extend my heartfelt congratulations.\033[0m
       .     "#:.    .:#"###"#:.    .:#"  .        .               \033[30mYour resilience, dedication, and compassion inspire us all.\033[0m
  .             "#########"#########"        .        .            \033[30mToday, we celebrate the valuable contributions of women like you,\033[0m
        .    "#:.  "####"###"####"  .:#"   .       .               \033[30mwho make the world a better place through their actions.\033[0m   
     .     .  "#######""##"##""#######"                  .         \033[30mYour strength, kindness, and unwavering support are not only appreciated but deeply cherished.\033[0m
                ."##"#####""#####"##"           .                  \033[30mThank you for being a beacon of hope and inspiration to everyone around you.\033[0m
   .   "#:. ...  .:##"###"###"###"##:. ... .:#"     .              \033[30mWith the utmost respect and admiration,\033[0m
      .     "#######"##"#####"##"#######"      .     .             \033[35m➡️ OUALID ELHADIM ➡️\033[0m
    .    .     "#####""#######""#####"    .      .               #nternational_Womens_Day #IWD2024
            .     "      \033[33m000\033[0m      "    .     .  
       .         .   .   \033[33m000\033[0m     .        .       .
........................\033[33m000\033[33m00\033[0m...............................
    """
    os.system('clear')
    print(picture.replace("#", "\033[32m#\033[0m"))
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./greeting.py [name]")

    else:
        name = sys.argv[1].capitalize()
        display_message(name)

