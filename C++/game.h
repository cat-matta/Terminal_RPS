#include <iostream>
#include<cctype> // for toupper
#include <time.h>
#include <string>
using std::string;
using namespace std;

bool match(char player,char pc){ // true indicates that you get point, false indicates pc gets point
	if(player=='r'){
		if(pc=='p') return false;
		if(pc=='s') return true;
	}
	else if(player=='p'){
		if(pc=='s') return false;
		if(pc=='r') return true;
	}
	else if(player=='s'){
		if(pc=='r') return false;
		if(pc=='p') return true;
	}
}

char convert_num(int num){ //to work for rand
	if(num==0) return 'r'; //0 looks like rock hehe
	if(num==1) return 'p'; //1 also like paper
	if(num==2) return 's'; //2 is just inverted s
}

string convert_char(char letter){ // just for fun
	if(letter=='p') return "Paper";
	if(letter=='r') return "Rock";
	if(letter=='s') return "Scissors";
}

void play_game(){
	int rounds,rounds_to_win;
	int player_score=0;
	int pc_score=0;
	char player_choice, pc_choice;
	cout<<"Let's begin, shall we? How many rounds do you want to play? \n";
	cin>>rounds;
	//win more than half of the games to win the game
	rounds_to_win=rounds/2+1; 
	cout<<"\nFirst to win "<<rounds_to_win<<" rounds wins\n";
	do{
		 //create random numbers between 0 to 100, then mod 3 to get 0 1 2
		pc_choice=convert_num((rand()%101)%3); //given the numbers from rand, convert it to a char
		cin>>player_choice;
		player_choice=tolower(player_choice); //upper or lower case doesnt matter
		cout<<"\nRock -- Paper -- Scissors -- Says -- Shoot\n";
		cout<< "\nI played: "<< convert_char(pc_choice)<< "\t  You played: "<<convert_char(player_choice)<<endl;
		
		if(pc_choice==player_choice) //no one wins
			cout<<"\t\tTie round"<<endl;
		
		else if(pc_choice!=player_choice){
			(match(player_choice,pc_choice) ? player_score++ : pc_score++); //whomst won the game
			cout<<(match(player_choice,pc_choice) ? "\tYou win this round \n" : "\tI win this round \n");
		}
		cout<<"MY SCORE: "<<pc_score<<"\tYOUR SCORE: "<<player_score<<endl;

		if(player_score==rounds_to_win||pc_score==rounds_to_win) break; //first to x rounds wins
		
	}while(player_choice!='q'); //player can exit game by pressing q

	if(pc_score>player_score) cout<< "\aI win this game\n";
	else if(pc_score<player_score) cout<< "\aYou win this game\n";
}