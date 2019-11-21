The most basic syntax for a directed flowchart is
 
Digraph G {
Nodename1 -> nodename2;
}
 
And produces:
 



Then you can easily (and very fast) scale the complexity. 
 
For example:
 
digraph G {
    
mynodename -> b;
m -> b;
a9 -> b;
c -> d0;
b -> c [label=" my labelled connection"];
c -> d1;
d0 -> e [label="CE"];
e -> d0 ;
f1 -> e;
f2 -> e;
g -> f1;
f1 -> h;
e -> z;
c -> y;
a9 [label="mylabellednode"]

}

Produces:



You can play around here:
http://dreampuf.github.io/GraphvizOnline/

Documentation and examples can be found here:
http://graphs.grevian.org/example
