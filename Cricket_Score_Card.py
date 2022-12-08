from time import sleep

def matches_data():
    """This funtion contain all the data of all the matches in the form of nested dictionaries and lists."""
    """Here 'India Vs Pakistan 23-10-2022' is the key which used to store all the data related to the match
           in the form of dictionary which is the value of 'India Vs Pakistan 23-10-2022'"""
    all_matches={
        "India Vs Pakistan 23-10-2022":{ 
            "match_id":1,
            "teams":{          #This key hold the name of the both teams, in the form of dictionary.
                "team_a":"India (IND)",
                "team_b":"Pakistan (PAK)"},
            "series":         #This key hold the details related to the type of series the match is, in the form of a list.
                ["International Cricket Council (ICC)",
                "Mens T20 World Cup",
                "2022",
                "Super 12",  
                "Group 2"],
            
            "date":"Sunday, October 23, 2022",  #This key hold the details related to the day and date the match was played.
            
            "time":"1:30 PM (IST)",  #This key hold the details related to the time the match was played.
            
            "venue":{      #This key hold the details related to the venue the match was played, in the form of a dictionary.
                "stadium":"Melbourne Cricket Ground",
                "city":"Melbourne"},
            
            "officials":{       #This key hold the details related to the officials of the match (like on-field and third umpiers etc.), in the form of a dictionary and list.
                "umpires":{
                    "on_field":[
                        "Marais Erasmus",
                        "Rod Tucker"],
                    "third_umpier":"Richard Kettleborough",
                    "reserve_umpire":"Joel Wilson"},
                "referee":"Ranjan Madugalle"},
            
            "team_members":{  #This key hold the names of the players that was the part of the match with thier position in the match, in the form of dictionary and list.
                "team_a_squad":{"captain":"Rohit Sharma","wicket keeper":"Dinesh Karthik",
                                "playing":["Rohit Sharma", "KL Rahul", "Virat Kohli","Suryakumar Yadav", "Hardik Pandya", "Dinesh Karthik", "Axar Patel", "Ravichandran Ashwin", "Bhuvneshwar Kumar", "Mohammed Shami", "Arshdeep Singh"],
                                "bench":["Harshal Patel", "Rishabh Pant", "Yuzvendra Chahal", "Deepak Hooda"]},
                "team_b_squad":{"captain":"Babar Azam","wicket keeper":"Mohammad Rizwan",
                                "playing":["Babar Azam", "Mohammad Rizwan", "Shan Masood","Shadab Khan", "Haider Ali", "Iftikhar Ahmed", "Mohammad Nawaz", "Asif Ali", "Shaheen Afridi", "Naseem Shah", "Haris Rauf"],
                                "bench":["Khushidil Shah", "Mohammad Hasnain", "Mohammad Wasim Jr.", "Fakhar Zaman"]}},
            
            "toss":{"winner":"India (IND)", "choose":"Bowl"},  #This key hold the details of the toss (the winner of the toss and their choice), in the form of dictionary.
            
            "overs":"20",  #This key contain total numbers of overs a match was.
            
            "match_winner":"India (IND)",  #This key contain the name of the winning team of the match.
            "wickets_remain":4,
            
            "runs":{"team_a_runs":160,"team_b_runs":159},  #This key contain the total run make by the both teams, in the form of dictionary.
            "wickets":{"team_a_wickets":6,"team_b_wickets":8}, #This key contain the total wickets of the both teams, in the the form of dictionary.
            
            "player_of_match":"Virat Kohli (IND)", #This key contain the name of the player of the match.
            
            "innings":{  #This key contain all the details related to both of the innings, in the form of dictionaries and lists.
                "inning_1":{  #This key contain all the details related to first innings, in the form of nested dictionaries and lists.
                    "batting":"Pakistan (PAK)",
                    "bowling":"India (IND)",
                    "opening_batsman":["Mohammad Rizwan","Babar Azam"],
                    "first_bowler":"Bhuvneshwar Kumar",
                    "total_6":6,
                    "total_4":12,
                    "bye":2,
                    "leg_bye":4,
                    "wide_ball":6,
                    "no_ball":1,
                    "run_rate":7.95,
                    "over_details":[  #This key contain the details related to the overs of 1st inning, in the form of nested lists.
                        #Here 'W' means Wicket, 'w' means wide ball, 'lb' means Leg-bye and 'b' means Bye
                        #In the format:- [1st ball, 2nd ball, 3rd ball, 4th ball, 5th ball, 6th ball, extra]
                        [0,0,0,0,0,"1w",0], 
                        ["W",0,0,0,1,4], 
                        ["1w",0,0,2,0,1,0],
                        [4,1,0,0,0,"W"],
                        [0,3,2,0,4,0], 
                        [0,0,4,3,0,1], 
                        [0,3,0,1,1,4], 
                        ["1w",0,"1lb",1,0,0,0], 
                        ["1lb",0,1,2,1,1], 
                        [2,1,1,4,1,"1lb"], 
                        [1,0,2,0,6,1], 
                        [6,0,6,6,0,3], 
                        [0,"W",0,4,0,1], 
                        [0,"W",0,2,0,"W"], 
                        [1,"1w",0,1,2,2,1], 
                        [1,4,0,4,"W",1], 
                        [1,2,1,"W",2,"1w",2], 
                        [0,4,4,0,1,1], 
                        [1,1,6,4,"1lb",1], 
                        ["1w",1,"W",6,0,0,"2b"]], 
                    "batsmen_details":[  #This key hold the detailed analysis of batsmen performance 1st inning in the match, in the form of nested lists.
                        #Format of the list:-[name of the batsmen, runs scored by the batsmen, total bowls played by the batsmen, total minutes the batsmen was on crease, total fours, total sixes]
                        ["Babar Azam",0,1,10,0,0], 
                        ["Mohammad Rizwan",4,12,25,1,0], 
                        ["Shan Masood",52,42,101,5,0], 
                        ["Shadab Khan",5,6,6,1,0], 
                        ["Haider Ali",2,4,6,0,0], 
                        ["Iftikhar Ahmed",51,34,43,2,4], 
                        ["Mohammad Nawaz",9,6,12,2,0], 
                        ["Asif Ali",2,3,6,0,0], 
                        ["Shaheen Afridi",16,8,17,1,1], 
                        ["Naseem Shah",0,0,0,0,0], 
                        ["Haris Rauf",6,4,3,0,1], 
                        ["Khushidil Shah",0,0,0,0,0], 
                        ["Mohammad Hasnain",0,0,0,0,0], 
                        ["Mohammad Wasim Jr.",0,0,0,0,0], 
                        ["Fakhar Zaman",0,0,0,0,0]], 
                    "bowler_details":[  #This key hold the detailed analysis of bowler performance 1st inning in the match, in the form of nested lists.
                        #Format of the list:-[name of the bowler, overs, maiden by the bowler, runs made against the bowler bowling, wickets taken by the bowler, total wide balls, total no balls
                        ["Rohit Sharma",0,0,0,0,0,0], 
                        ["KL Rahul",0,0,0,0,0,0], 
                        ["Virat Kohli",0,0,0,0,0,0], 
                        ["Suryakumar Yadav",0,0,0,0,0,0], 
                        ["Hardik Pandya",4,0,30,3,0,0], 
                        ["Dinesh Karthik",0,0,0,0,0,0], 
                        ["Axar Patel",1,0,21,0,0,0], 
                        ["Ravichandran Ashwin",3,0,23,0,0,1], 
                        ["Bhuvneshwar Kumar",4,0,22,1,0,3], 
                        ["Mohammed Shami",4,0,25,1,0,1], 
                        ["Arshdeep Singh",4,0,32,3,0,1], 
                        ["Harshal Patel",0,0,0,0,0,0], 
                        ["Rishabh Pant",0,0,0,0,0,0], 
                        ["Yuzvendra Chahal",0,0,0,0,0,0], 
                        ["Deepak Hooda",0,0,0,0,0,0]],
                    },
                "inning_2":{  #This key contain all the details related to second innings, in the form of nested dictionaries and lists.
                    "batting":"India (IND)",
                    "bowling":"Pakistan (PAK)",
                    "opening_batsman":["KL Rahul","Rohit Sharma"],
                    "first_bowler":"Shaheen Afridi",
                    "total_6":6,
                    "total_4":9,
                    "bye":3,
                    "leg_bye":1,
                    "wide_ball":6,
                    "no_ball":1,
                    "run_rate":8.00,
                    "over_details":[ #This key contain the details related to the overs of 2st inning, in the form of nested lists.
                        #Here 'W' means Wicket, 'w' means wide ball, 'lb' means Leg-bye and 'b' means Bye
                        #In the format:-[1st ball, 2nd ball, 3rd ball, 4th ball, 5th ball, 6th ball, extra]
                        [0,1,1,1,0,2], 
                        [0,0,2,0,"W",0], 
                        [0,1,0,2,0,0],
                        [0,"W",4,3,0,0],
                        [0,0,3,1,0,1], 
                        [0,4,"W",2,"1lb",2], 
                        ["W",0,1,0,1,0], 
                        [1,0,1,1,1,1], 
                        [1,1,0,0,0,1], 
                        [0,1,2,0,0,1], 
                        [0,4,1,1,1,2], 
                        [6,1,0,6,1,6], 
                        [1,2,1,4,1,0], 
                        [4,1,0,1,0,1], 
                        [2,1,1,4,1,1], 
                        [0,1,0,1,"3w",0,1], 
                        [1,2,0,1,0,2], 
                        [4,"1w",2,4,1,1,4], 
                        [1,1,0,1,6,6], 
                        ["W",1,2,"7nb","1w","3b","W","1w",1]], 
                    "batsmen_details":[ #This key hold the detailed analysis of batsmen performance 2nd inning in the match, in the form of nested lists.
                        #Format of the list:-[name of the batsmen, runs scored by the batsmen, total bowls played by the batsmen, total minutes the batsmen was on crease, total fours, total sixes]
                        ["Rohit Sharma",4,7,20,0,0], 
                        ["KL Rahul",4,8,13,0,0], 
                        ["Virat Kohli",82,53,98,6,4], 
                        ["Suryakumar Yadav",15,10,11,2,0], 
                        ["Hardik Pandya",40,37,61,1,2], 
                        ["Dinesh Karthik",1,2,10,0,0], 
                        ["Axar Patel",2,3,7,0,0], 
                        ["Ravichandran Ashwin",1,1,2,0,0], 
                        ["Bhuvneshwar Kumar",0,0,0,0,0], 
                        ["Mohammed Shami",0,0,0,0,0], 
                        ["Arshdeep Singh",0,0,0,0,0], 
                        ["Harshal Patel",0,0,0,0,0], 
                        ["Rishabh Pant",0,0,0,0,0], 
                        ["Yuzvendra Chahal",0,0,0,0,0], 
                        ["Deepak Hooda",0,0,0,0,0]],
                    "bowler_details":[ #This key hold the detailed analysis of bowler performance 2nd inning in the match, in the form of nested lists.
                        #Format of the list:-[name of the bowler, overs, maiden by the bowler, runs made against the bowler bowling, wickets taken by the bowler, total wide balls, total no balls]
                        ["Babar Azam",0,0,0,0,0,0], 
                        ["Mohammad Rizwan",0,0,0,0,0,0], 
                        ["Shan Masood",0,0,0,0,0,0], 
                        ["Shadab Khan",4,0,21,0,0,0], 
                        ["Haider Ali",0,0,0,0,0,0], 
                        ["Iftikhar Ahmed",0,0,0,0,0,0], 
                        ["Mohammad Nawaz",4,0,42,2,2,1], 
                        ["Asif Ali",0,0,0,0,0,0], 
                        ["Shaheen Afridi",4,0,34,0,1,0], 
                        ["Naseem Shah",4,0,23,1,0,0], 
                        ["Haris Rauf",4,0,36,2,1,0], 
                        ["Khushidil Shah",0,0,0,0,0,0], 
                        ["Mohammad Hasnain",0,0,0,0,0,0], 
                        ["Mohammad Wasim Jr.",0,0,0,0,0,0], 
                        ["Fakhar Zaman",0,0,0,0,0,0]], 
                    }
                }
            }
        }
    
    return all_matches

def search_match():
    """This funtion is to search and check weather the match details are available or not in the matches_data()"""
    
    #Here we have use global keyword to convert match_between into global variable so that this varible can used in multiple location.
    global match_between 
    
    print("\n===================================================================================================")
    print("                                         SEARCH MATCHES                                            ")
    print("===================================================================================================\n")
    print("The Available match are as followed:")
    print("---------------------------------------------------------------------------------------------------")
    for avl_match in matches_data().keys():
        print("Match Id:",matches_data()[avl_match]["match_id"])
        avl_match=avl_match.split(" ")
        print("Match Between:",end=" ")
        for value in range(3):
            print(avl_match[value],end=" ")
        print("\nMatch Date:",avl_match[3])
        print("---------------------------------------------------------------------------------------------------")
    match=str(input("Enter the Name of the Teams seprated by (vs) from above list:"))  #This varible store the name of the match enterd by the user, in the form of string
    """Format of the string which is going to store inside (match):- <name of team A> vs <name of team B>"""
    date=str(input("Enter the Date of the Match in (dd-mm-yyyy):"))  #This varible store the date of the match enterd by the user, in the form of string
    """Format of the string which is going to store inside (date):- dd-mm-yyyy"""
    match_between=(match+" "+date) #This variable store the string which is form by concatenatation of variable match and variable date.
    """match_between store the name of the match which should be searched in the matches_data() function."""
    """This if-else statement search the match_between or match_id in matches_data() and redirect the user to the match_details()
       function if the match is present in the match_data(), else it will print no match found and give the user the option to retry."""
    if (match_between.title() in matches_data().keys()):
        """This if statement search whether match_between is present in the matches_data()
           if true than it will call clear() and match_details() functions"""
        clear()
        match_details()
    else:
        print("Sorry!")
        print("No Match Found.\n")
        search_again=str(input("Do you wanted to try again yes or no:"))
        if (search_again.upper()=="YES" or search_again.upper()=="Y"):
            clear()
            search_match()
        else:
            back_main_menu()

def team_members():
    """This function is use to print all the data related to the team members which are store in the matches_data() function."""
    print("\n===================================================================================================")
    print("                                           TEAM MEMBERS                                            ")
    print("===================================================================================================\n")
    
    #This print statements print the name of the team A.
    print("TEAM",(match["teams"]["team_a"].upper())+":")
    print("*"*(len((match["teams"]["team_a"].upper())+":")+5))
    
    #This print statements print the name of the captain of team A
    print("\nCAPTAIN:\n^^^^^^^^")
    print(match["team_members"]["team_a_squad"]["captain"])
    
    #This print statements print the name of the wicket keeper of team A
    print("\nWICKET KEEPER:\n^^^^^^^^^^^^^^")
    print(match["team_members"]["team_a_squad"]["wicket keeper"])
    
    #This print statements print the name of all the playing members of team A using for loop
    print("\nPLAYING:\n^^^^^^^^")
    for player in (match["team_members"]["team_a_squad"]["playing"]):
        print(">"+player)
        
    #This print statements print the name of all the bench members of team A using for loop
    print("\nBENCH:\n^^^^^^")
    for player in (match["team_members"]["team_a_squad"]["bench"]):
        print(">"+player)
        
    #This print statements print the name of the team B.
    print("\n\nTEAM",(match["teams"]["team_b"].upper())+":")
    print("*"*(len((match["teams"]["team_b"].upper())+":")+5))
    
    #This print statements print the name of the captain of team B
    print("\nCAPTAIN:\n^^^^^^^^")
    print(match["team_members"]["team_b_squad"]["captain"])
    
    #This print statements print the name of the wicket keeper of team B
    print("\nWICKET KEEPER:\n^^^^^^^^^^^^^^")
    print(match["team_members"]["team_b_squad"]["wicket keeper"])
    
    #This print statements print the name of all the playing members of team B using for loop
    print("\nPLAYING:\n^^^^^^^^")
    for player in (match["team_members"]["team_b_squad"]["playing"]):
        print(">"+player)
        
    #This print statements print the name of all the bench members of team B using for loop
    print("\nBENCH:\n^^^^^^")
    for player in (match["team_members"]["team_b_squad"]["bench"]):
        print(">"+player)
    
    #This statements are to give user option to go back. 
    ans=str(input("\n\nDo you wanted to go Back? (Yes or No):"))
    if ((ans.upper()=="YES") or (ans.upper()=="Y")):
        clear()
        match_details()
    else:
        extended_clear()
        team_members()

def officials():
    """This function is use to print all the data related to the official of the match which are store in the matches_data() function."""
    print("\n===================================================================================================")
    print("                                          MATCH OFFICIALS                                          ")
    print("===================================================================================================\n")
    
    #This print statements print data names of the umpires of the match, it contains: on-field umpiers, third umpire and reserve umpire.
    print("UMPIRES:\n********")
    print("\nON-FIELD UMPIRES:\n^^^^^^^^^^^^^^^^^")
    for umpiers in (match["officials"]["umpires"]["on_field"]):
        print(">"+umpiers)
    print("\nTHIRD UMPIRE\n^^^^^^^^^^^^^^")
    print(match["officials"]["umpires"]["third_umpier"])
    print("\nRESERVE UMPIRES:\n^^^^^^^^^^^^^^^^")
    print(match["officials"]["umpires"]["reserve_umpire"])
    
    #This print statements print name of the referee.
    print("\nREFEREE:\n********")
    print(match["officials"]["referee"])
    
    #This statements are to give user option to go back.
    ans=str(input("\n\nDo you wanted to go Back? (Yes or No):"))
    if ((ans.upper()=="YES") or (ans.upper()=="Y")):
        clear()
        match_details()
    else:
        extended_clear()
        officials()

def inning1():
    """This function is use to print all the data related to the first inning of the match which are store in the matches_data() function."""
    print("\n===================================================================================================")
    print("                                        FIRST INNING DETAILS                                       ")
    print("===================================================================================================\n")
    
    #This varible is to store dictionary that store all of the data related to first inning of the match.
    inning=(match["innings"]["inning_1"])
    
    #This print statements print the name of the batting team.
    print("BATTING TEAM:\n*************")
    print(inning["batting"])
    
    #This print statements print the name of the bowling team.
    print("\nBOWLING TEAM:\n*************")
    print(inning["bowling"])
    
    #This print statements print the name of the opening batsmen using for loop.
    print("\nOPENING BATSMAN:\n****************")
    for names in (inning["opening_batsman"]):
        print(">"+names)
        
    #This print statements print the name of the first bowler.
    print("\nFIRST BOWLER:\n*************")
    print(inning["first_bowler"])
    
    #This print statements print total number of sixes.
    print("\nTOTAL 6's:\n**********")
    print(inning["total_6"])
    
    #This print statements print total number of fours.
    print("\nTOTAL 4's:\n**********")
    print(inning["total_4"])
    
    #This print statements print total number of bye.
    print("\nTOTAL BYE:\n**********")
    print(inning["bye"])
    
    #This print statements print total number of leg-bye.
    print("\nTOTAL LEG-BYE:\n**************")
    print(inning["leg_bye"])
    
    #This print statements print total number of wide balls.
    print("\nTOTAL WIDE BALL:\n****************")
    print(inning["wide_ball"])
    
    #This print statements print total number of no balls.
    print("\nTOTAL NO BALL:\n**************")
    print(inning["no_ball"])
    
    #This print statements print the overall run rate of the inning.
    print("\nRUN RATE:\n*********")
    print(inning["run_rate"])
    
    #This print statements print over wise details of the inning using for loop.
    print("\nOVER DETAILS:\n*************")
    num=1
    for overs in (inning["over_details"]):
        string="Over "+str(num)+":"
        print(string,end="")
        for i in overs:
            print(i,end=", ")
        num=num+1
        print()
    
    #This print statements print batsmen performance details using for loop.
    print("\nBATSMEN DETAILS:\n****************")  
    for bat in (inning["batsmen_details"]):
        print(">"+bat[0])
        print("  Runs:",bat[1])
        print("  Balls:",bat[2])
        print("  Minutes on Crease:",bat[3])
        print("  Fours:",bat[4])
        print("  Sixes:",bat[5])
        print()
        
    #This print statements print bowler performance details using for loop.
    print("\nBOWLER DETAILS:\n***************")  
    for ball in (inning["bowler_details"]):
        print(">"+ball[0])
        print("  Overs:",ball[1])
        print("  Maiden:",ball[2])
        print("  Runs:",ball[3])
        print("  Wickets:",ball[4])
        print("  Wide Balls:",ball[5])
        print("  No Balls:",ball[6])
        print() 
        
    #This statements are to give user option to go back.
    ans=str(input("\n\nDo you wanted to go Back? (Yes or No):"))
    if ((ans.upper()=="YES") or (ans.upper()=="Y")):
        clear()
        match_details()
    else:
        extended_clear()
        inning1()

def inning2():
    """This function is use to print all the data related to the first inning of the match which are store in the matches_data() function."""
    print("\n===================================================================================================")
    print("                                        SECOND INNING DETAILS                                      ")
    print("===================================================================================================\n")
    
    #This varible is to store dictionary that store all of the data related to second inning of the match.
    inning=(match["innings"]["inning_2"])
    
    #This print statements print the name of the batting team.
    print("BATTING TEAM:\n*************")
    print(inning["batting"])
    
    #This print statements print the name of the bowling team.
    print("\nBOWLING TEAM:\n*************")
    print(inning["bowling"])
    
    #This print statements print the name of the opening batsmen using for loop.
    print("\nOPENING BATSMAN:\n****************")
    for names in (inning["opening_batsman"]):
        print(">"+names)
        
    #This print statements print the name of the first bowler.
    print("\nFIRST BOWLER:\n*************")
    print(inning["first_bowler"])
    
    #This print statements print total number of sixes.
    print("\nTOTAL 6's:\n**********")
    print(inning["total_6"])
    
    #This print statements print total number of fours.
    print("\nTOTAL 4's:\n**********")
    print(inning["total_4"])
    
    #This print statements print total number of bye.
    print("\nTOTAL BYE:\n**********")
    print(inning["bye"])
    
    #This print statements print total number of leg-bye.
    print("\nTOTAL LEG-BYE:\n**************")
    print(inning["leg_bye"])
    
    #This print statements print total number of wide balls.
    print("\nTOTAL WIDE BALL:\n****************")
    print(inning["wide_ball"])
    
    #This print statements print total number of no balls.
    print("\nTOTAL NO BALL:\n**************")
    print(inning["no_ball"])
    
    #This print statements print the overall run rate of the inning.
    print("\nRUN RATE:\n*********")
    print(inning["run_rate"])
    
    #This print statements print over wise details of the inning using for loop.
    print("\nOVER DETAILS:\n*************")
    num=1
    for overs in (inning["over_details"]):
        string="Over "+str(num)+":"
        print(string,end="")
        for i in overs:
            print(i,end=", ")
        num=num+1
        print()
    
    #This print statements print batsmen performance details using for loop.
    print("\nBATSMEN DETAILS:\n****************")  
    for bat in (inning["batsmen_details"]):
        print(">"+bat[0])
        print("  Runs:",bat[1])
        print("  Balls:",bat[2])
        print("  Minutes on Crease:",bat[3])
        print("  Fours:",bat[4])
        print("  Sixes:",bat[5])
        print()
        
    #This print statements print bowler performance details using for loop.
    print("\nBOWLER DETAILS:\n***************")  
    for ball in (inning["bowler_details"]):
        print(">"+ball[0])
        print("  Overs:",ball[1])
        print("  Maiden:",ball[2])
        print("  Runs:",ball[3])
        print("  Wickets:",ball[4])
        print("  Wide Balls:",ball[5])
        print("  No Balls:",ball[6])
        print() 
        
    #This statements are to give user option to go back.
    ans=str(input("\n\nDo you wanted to go Back? (Yes or No):"))
    if ((ans.upper()=="YES") or (ans.upper()=="Y")):
        clear()
        match_details()
    else:
        extended_clear()
        inning1()
        
def match_details():
    """This function is use to print all the basic data rlated to the match which are store in the matches_data() function.
    like match timing, match date, match venue etc."""
    global match
    print("\n===================================================================================================")
    print("                                          MATCHES DETAILS                                          ")
    print("===================================================================================================\n")
    
    #This varible is to store all of the data related to the match which is present in matches_data() function.
    match=(matches_data()[match_between.title()])
    
    #This print statements print the name of the teams.
    print("MATCH:\n******")
    print(match["teams"]["team_a"],"VS",match["teams"]["team_b"])
    
    #This print statements print details related to the series of the match using for loop.
    print("\nSERIES:\n*******")
    for data in match["series"]:
        print(data)
        
    #This print statements print the match date.
    print("\nMATCH DATE:\n***********")
    print(match["date"])
    
    #This print statements print the match timing.
    print("\nMATCH TIMING:\n*************")
    print(match["time"])
    
    #This print statements print the match venue.
    print("\nMATCH VENUE:\n************")
    print(match["venue"]["stadium"],match["venue"]["city"],sep=", ")
    
    #This print statements print the total number of overs the match have.
    print("\nOVERS:\n******")
    print(match["overs"])
    
    #This print statements print the name toss winner and their pick (bowling or batting).
    print("\nTOSS WINNER:\n************")
    print(match["toss"]["winner"],"and choose to",match["toss"]["choose"],"first")
    
    #This print statements print the name match winner with remaining wickets.
    print("\nMATCH WINNER:\n**************")
    print(match["match_winner"],"won by",match["wickets_remain"],"wickets")
    
    #This print statements print the score of both teams with total wickets.
    print("\nSCORES:\n*******")
    print(match["teams"]["team_a"],"score:",str(match["runs"]["team_a_runs"])+"/"+str(match["wickets"]["team_a_wickets"]))
    print(match["teams"]["team_b"],"score:",str(match["runs"]["team_b_runs"])+"/"+str(match["wickets"]["team_b_wickets"]))
    
    #This print statements print the name of man of the match.
    print("\nMAN OF THE MATCH:\n*****************")
    print(match["player_of_match"])
    
    """This print statements are used to print the options that user can use to access information relating to the match."""
    print("\n\nFor More details select form the options given below:")
    print("1.Team Members")
    print("2.Officials")
    print("3.First Inning")
    print("4.Second Inning")
    print("5.Back")
    
    
    #This if-elif-else statements are used to call specific function depending on the input given by the user.
    option=str(input("Enter your pick here:"))
    option=option.upper()
    if ((option in ["1","01"]) or (option=="TEAM MEMBERS")):
        #This if statement will call team_members() and clear() functions if user input is 1,01 or TEAM MEMBERS. 
        clear()
        team_members()
    elif ((option in ["2","02"]) or (option=="OFFICIALS")):
        #This elif statement will call officials() and clear() functions if user input is 2,02 or OFFICIALS. 
        clear()
        officials()
    elif ((option in ["3","03"]) or (option=="FIRST INNING")):
        #This elif statement will call inning1() and clear() functions if user input is 3,03 or FIRST INNING. 
        clear()
        inning1()
    elif ((option in ["4","04"]) or (option=="SECOND INNING")):
        #This elif statement will call inning2() and clear() functions if user input is 4,04 or SECOND INNING. 
        clear()
        inning2()
    elif ((option in ["5","05"]) or (option=="BACK")):
        #This elif statement will call main_menu() and clear() functions if user input is 5,05 or BACK. 
        clear()
        main_menu()
    else:
        #This else statement will call match_details() and extended_clear() function if user input is some thing else then the provided options with an error message. 
        print("Error!, Invalid Input.")
        print("Please Choose the correct option.\n")
        extended_clear()
        match_details()

def clear():
    """This function is to clear the output that is displayed on the terminal/console/kernel"""
    #Note:This funtion work in Jupiter notebook but due to some internal coding of Jupiter notebook the output does not get display.
    print("===================================================================================================")
    sleep(0.5) #This is the funtion of module time which is used to give delay for certain seconds depending on user.
    print("\033[H\033[J") #This is a ASCII code which is use to clear the output.
    sleep(0.2)

def extended_clear():
    """This function is to clear the output that is displayed on the terminal/console/kernel. But run slow then clear() function"""
    #Note:This funtion work in Jupiter notebook but due to some internal coding of Jupiter notebook the output does not get display.
    print("===================================================================================================")
    sleep(1.5)
    print("\033[H\033[J") #This is a ASCII code which is use to clear the output.
    sleep(0.2)

def Quit():
    """This function is call when user whanted to exit the application/program"""
    clear()
    #This is the greeting text that will be printed at the end to say thank you to user for using the program.
    print("\n===================================================================================================\n")
    print(" .-') _    ('-. .-.   ('-.         .-') _ .-. .-')                                            ,---.    ")
    print("(  OO) )  ( OO )  /  ( OO ).-.    ( OO ) )\  ( OO )                                           |   |    ")
    print("/     '._ ,--. ,--.  / . --. /,--./ ,--,' ,--. ,--.       ,--.   ,--..-'),-----.  ,--. ,--.   |   |    ")
    print("|'--...__)|  | |  |  | \-.  \ |   \ |  |\ |  .'   /        \  `.'  /( OO'  .-.  ' |  | |  |   |   |    ")
    print("'--.  .--'|   .|  |.-'-'  |  ||    \|  | )|      /,      .-')     / /   |  | |  | |  | | .-') |   |    ")
    print("   |  |   |       | \| |_.'  ||  .     |/ |     ' _)    (OO  \   /  \_) |  |\|  | |  |_|( OO )|  .'    ")
    print("   |  |   |  .-.  |  |  .-.  ||  |\    |  |  .   \       |   /  /\_   \ |  | |  | |  | | `-' /`--'     ")
    print("   |  |   |  | |  |  |  | |  ||  | \   |  |  |\   \      `-./  /.__)   `'  '-'  '('  '-'(_.-' .--.     ")
    print("   `--'   `--' `--'  `--' `--'`--'  `--'  `--' '--'        `--'          `-----'   `-----'    '--'     ")
    print("\n===================================================================================================\n")

def back_main_menu():
    """This is the function which is called to go back to the main menu window"""
    clear()
    main_menu()

def old_match():
    """This funtion is provide user the option to use the search_match() function."""
    print("\n===================================================================================================")
    print("                                           OLD MATCHES                                             ")
    print("===================================================================================================\n")
    """This print statements are used to print the options that user can use to access information relating to the match."""
    print("1.Search Match")
    print("2.Back")

    #This if-elif-else statements are used to call specific function depending on the input given by the user.
    print("\nEnter the Number or the name of the Feature you wanted to use.")
    option=str(input("Enter your pick here:"))
    option=option.upper()
    if ((option in ["1","01"]) or (option=="SEARCH MATCH")):
        #This if statement will call search_match() and clear() functions if user input is 1,01 or SEARCH MATCH. 
        clear()
        search_match()
    elif ((option in ["2","02"]) or (option=="BACK")):
        #This elif statement will call back_main_menu() functions if user input is 2,02 or BACK. 
        back_main_menu()
    else:
        #This else statement will call old_match() and extended_clear() function if user input is some thing else then the provided options with an error message.
        print("Error!, Invalid Input.")
        print("Please Choose the correct option.\n")
        extended_clear()
        old_match()
    
def main_menu():
    print("\n===================================================================================================")
    print("                                             MAIN MENU                                             ")
    print("===================================================================================================\n")
    print("1.Old Matches")
    print("2.Quit")
    print("\nEnter the Number or the name of the Feature you wanted to use.")
    option=str(input("Enter your pick here:"))
    
    option=option.upper()
    if ((option in ["1","01"]) or (option=="OLD MATCHES")):
        #This elif statement will call old_match() and clear() functions if user input is 1,01,OLD MATCHES.
        clear()
        old_match()
    elif ((option in ["2","02"]) or (option=="QUIT")):
        #This elif statement will call Quit() function if user input is 2,02,QUIT.
        Quit()
    else:
        #This else statement will call main_menu() and extended_clear() function if user input is some thing else then the provided options with an error message.
        print("Error!, Invalid Input.")
        print("Please Choose the correct option.\n")
        extended_clear()
        main_menu()

#This is the first function which will be called to run the application. 
main_menu()