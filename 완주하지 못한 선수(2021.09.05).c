#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    unordered_map<string, int> hashmap;
    for (int i = 0 ; i < completion.size() ; i++){
        if(hashmap.find(completion[i]) != hashmap.end()) hashmap[completion[i]] += 1;
        else hashmap[completion[i]] = 1;
    }
    
    for (int i = 0 ; i < participant.size() ; i++){
        if(hashmap.find(participant[i]) == hashmap.end()) {
            answer = participant[i];
            break;
        }else{
            if(hashmap[participant[i]] == 1){
                hashmap.erase(participant[i]);
            }else{
                hashmap[participant[i]] -= 1;
            }
        }
    }
    
    return answer;
}