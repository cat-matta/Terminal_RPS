
#include <iostream>
#include<cctype> // for toupper
#include "game.h"
#include <time.h> //for rand
#include <string>
using std::string;
using namespace std;

int main(){
	cout<<"To play, simply choose: (R)ock \t(P)apper \tor (S)cissors\n";
	cout<<"Entering uppercase is optional\nPress q at anytime to exit\n";
	cout<<"Are you ready to play? (Y) (N) \t";
	char choice;
	cin>>choice;
	choice=toupper(choice); //makes it easy to put any choice, upper or lower
	srand(time(NULL)); //for making rand more efficient
	while(choice=='Y'&&choice!='N'&&choice!='Q'){
		play_game();
		cout<<"Do you want to play again? \t";
		cin>>choice;
		choice=toupper(choice);
	}
	cout<<"\t~~~\aGoodbye!~~~"<<endl;
}