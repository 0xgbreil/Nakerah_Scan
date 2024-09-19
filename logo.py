def banner():
    import time
    
    banner = [
        "███╗░░██╗░█████╗░██╗░░██╗███████╗██████╗░░█████╗░██╗░░██╗  ░██████╗░█████╗░░█████╗░███╗░░██╗",
        "████╗░██║██╔══██╗██║░██╔╝██╔════╝██╔══██╗██╔══██╗██║░░██║  ██╔════╝██╔══██╗██╔══██╗████╗░██║",
        "██╔██╗██║███████║█████═╝░█████╗░░██████╔╝███████║███████║  ╚█████╗░██║░░╚═╝███████║██╔██╗██║",
        "██║╚████║██╔══██║██╔═██╗░██╔══╝░░██╔══██╗██╔══██║██╔══██║  ░╚═══██╗██║░░██╗██╔══██║██║╚████║",
        "██║░╚███║██║░░██║██║░╚██╗███████╗██║░░██║██║░░██║██║░░██║  ██████╔╝╚█████╔╝██║░░██║██║░╚███║",
        "╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝  ╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝"
    ]
    
    colors = range(7)
    
    try:
        for _ in range(1):
            for color in colors:
                for line in banner:
                    print(f"\033[1;3{color}m{line}")
                time.sleep(0.3)
                print("\033[H\033[J", end='')
                
        
        for line in banner:
            print(line)
        print("\033[1;37m𝘽𝙮 𝙈𝙤𝙝𝙖𝙢𝙚𝙙 𝙂𝙗𝙧𝙚𝙞𝙡\033[0m")  
        print ("")
        blue_light = '\033[94m'  
        yellow = '\033[93m'      
        reset = '\033[0m'        
        print(f"{yellow}LinkedIn : {blue_light}https://www.linkedin.com/in/mohammed-gbreil-b07382329/{reset}")

    except KeyboardInterrupt:
        pass

banner()

