#include<stdio.h>
#include<string.h>

int main(){
  char buf[32];
  char key[]="game_security";

  puts("Please input the passphrase");
  fgets(buf,sizeof(buf),stdin);

  strtok(buf,"\n");
  if(!strcmp(buf,key)){
    puts("congraturaltion!lctf{line_game_security_one_of_the_inportant}");
  }else{
    puts("invalid inputs");
  }
  return(0);
}
