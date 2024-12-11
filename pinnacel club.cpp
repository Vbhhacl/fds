#include <iostream>
#include<string.h>
using namespace std;
struct node 
{
int PRN;
char Name[50];
struct  node *next, *data;
};

class info 
{
public:
int a;
char b[50];
void addmember();
void addpresident();
void show();
void deletepres();
void deletemem();
void deletesecretary ();
node *create();
node *head =NULL , *temp=NULL;
};

node *info::create()
{
node *p=new(struct node);
cout<<"enter PRN number : ";
cin>>a;
p->PRN=a;
cout<<"enter name : ";
cin>>b;
strcpy(p->Name,b);
p->next=NULL;
return (p);
}

void info:: addmember()
{
node  *p=create();
if(head==NULL)
{
head=p;
}
else
{
temp=head;
while (temp->next!=NULL)
{
temp=temp->next;
}
temp->next=p;
}
}

void info:: addpresident()
{
node  *p=create();
if(head==NULL)
{
p=head;
}
else 
{
temp=head;
head=p;
head->next=temp;
}
}

void info ::show()
{
temp=head;
cout<<" \n" << "PRN NO. " << "         "  <<"NAME"<<endl;
while(temp!=NULL)
{
cout<<"  \n" << temp->PRN  << "         "  << temp-> Name<<endl ;
temp=temp->next;
}
}

void info :: deletepres ()
{
node *p;
p=head;
head=head->next;
p->next=NULL;
delete(p);
}
void info :: deletesecretary ()
{
node *p;
p=head;
while (p->next!=NULL)
{
temp=p;
p=p->next;
}
temp->next=NULL;
delete(p);
}

void info :: deletemem()
{
node *p,*temp;
p=head;
while (p->data!=NULL)
{
temp=p;
p=p->next;
}
temp->next=p->next;
p=p->next;
}

int main()
{
info c;
int ch;
do
{
cout<<" MENU  "<<endl;
cout<<"1. add members "<<endl;
cout<<"2.add  president"<<endl;
cout<<"3.add secretary "<<endl;
cout<<"4.display"<<endl;
cout<<"5. delete president"<<endl;
cout<<"6. delete member"<<endl;
cout<<"7. delete secretary"<<endl;
cout<<"8.exit"<<endl;
cout<<"enter your choice  : ";
cin>>ch;
switch(ch)
{	case 1:  {c.addmember();
		       break;}
	case 2: {c.addpresident();
		       break;}
	case 3:{ c.addmember();
		       break;}
	case 4: {c.show();
		      break;}
	case 5: {c.deletepres();
			 break;}
	 case 6: {c.deletemem();
			 break;}	
	 case 7:{c.deletesecretary();
			 break;}			 	      
	case 8: exit(0);
}
}	
while (ch!=8);	
return 0;
}
