/*
Sarah Johanknecht johankn1@black
2016-09-14
simplesystem.cpp

Simple System to replicate findings of papers on Spatial Heterogeneity
*/

#include <iostream>
using std::cout;

#include <cmath>
using std::fabs;
using std::sqrt;

#include "../Empirical/evo/World.h"
#include "../Empirical/tools/Random.h"

//Create an organism declared using an array of 3 doubles (x-coordinate, y-coordinate, environmental variable)
using org_type = std::array<double, 3>;

//Declare variables ** These can be changed **
double MUT_RATE=0.01; //standard deviation
double TOURN_SIZE=5; //size of tournament for tournament selection
int POP_SIZE=10; //size of population
int GEN_SIZE=100; //number of generations

int main()
{
	//Create a Random Number Generator with random seed (-1 is default that tells generator to choose a random seed)
	emp::Random random(-1);
	
	//Create World, using org_type as organism and LineagePruned lineage tracker
	emp::evo::World<org_type, emp::evo::LineageStandard, emp::evo::DefaultStats> world(random, "simpleWorld");
	
	world.statsM.fit_fun= [] (org_type* org) {return (sqrt(2) - fabs((*org)[0]-(*org)[2]));};
	
	for(int i=0; i<POP_SIZE; i++)
	{
		//Create an organism array
		std::array<double, 3> next_org;
		
		//Fill organism array with 3 doubles (x,y, environmental variable) between 0 and 1
		for(int j=0; j<3; j++)
		{
			next_org[j]= random.GetDouble();
		}
		
		world.Insert(next_org);
	
		
	}	
	
	//Loop through the generations
	for(int i=0; i<GEN_SIZE;i++)
	{		
		//Use MutatePop function to mutate the organism (using created lamda function)
		world.MutatePop([] (org_type* org, emp::Random& random) {random.GetRandNormal(0,MUT_RATE); 
			for(int j=0; j<3; j++){
				(*org)[j] += random.GetRandNormal(0,MUT_RATE);};
			return true;});
			
		//Run Tournament Selection on population
		world.TournamentSelect([] (org_type* org) {return (sqrt(2) - fabs((*org)[0]-(*org)[2]));}, TOURN_SIZE, POP_SIZE);
		
		world.Update();
	}
	
	world.lineageM.WriteDataToFile("lineageData.json");
}
	
	



