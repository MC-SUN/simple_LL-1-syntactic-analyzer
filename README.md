# simple LL(1)-syntactic-analyzer 简单的LL(1)语法分析器
Practice compiler theory courses: design, compile and debug an LL(1) parser, use the parser to recognize the symbol string, deepen the understanding of the grammar analysis principle.
设计、编制、调试一个LL(1)语法分析器，利用语法分析器对符号串的识别，加深对语法分析原理的理解。
# Content
1. Detect and remove direct left recursion;
2. Solve the FIRST set and FOLLOW set;
3. Build LL(1) analysis table;
4. Build LL analysis program, which can analyze the sentences input by the user with the constructed analysis program and show the analysis process.
1、检测去除直接左递归；
2、求解FIRST集和FOLLOW集；
3、构建LL(1)分析表；
4、构建LL分析程序，对于用户输入的句子，能够利用所构造的分析程序进行分析，并显示出分析过程。
#epsilon=="ε"
## Others
1. Adjust {:10s}{:20s} when the length of the input string is greater than 7
2. Remove direct left recursion
1. 当输入字符串长度大于7时，调整{:10s}{:20s}
2. 去除直接左递归
# Example
## test data: G = {"E": "E+T|ε|T", "T": "T*F|F", "F": "(E)|i"}
![image](https://github.com/MC-SUN/simple_LL-1-syntactic-analyzer/blob/master/example/1.png)
![image](https://github.com/MC-SUN/simple_LL-1-syntactic-analyzer/blob/master/example/2.png)
![image](https://github.com/MC-SUN/simple_LL-1-syntactic-analyzer/blob/master/example/3.png)
![image](https://github.com/MC-SUN/simple_LL-1-syntactic-analyzer/blob/master/example/4.png)
# License:
Copyright (c) 2020 Sun Yangyang. Free for use
