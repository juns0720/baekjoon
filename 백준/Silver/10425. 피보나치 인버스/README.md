# [Silver II] 피보나치 인버스 - 10425 

[문제 링크](https://www.acmicpc.net/problem/10425) 

### 성능 요약

메모리: 550668 KB, 시간: 600 ms

### 분류

임의 정밀도 / 큰 수 연산, 이분 탐색

### 제출 일자

2025년 2월 16일 16:59:00

### 문제 설명

<p><mjx-container class="MathJax" jax="CHTML" display="true" style="font-size: 109%; position: relative;"> <mjx-math display="true" class="MJX-TEX" aria-hidden="true" style="margin-left: 0px; margin-right: 0px;"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D439 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.106em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c3D"></mjx-c></mjx-mo><mjx-mrow space="4"><mjx-mo class="mjx-n"><mjx-stretchy-v class="mjx-c7B" style="height: 3.4em; vertical-align: -1.45em;"><mjx-beg><mjx-c></mjx-c></mjx-beg><mjx-ext><mjx-c></mjx-c></mjx-ext><mjx-mid><mjx-c></mjx-c></mjx-mid><mjx-ext><mjx-c></mjx-c></mjx-ext><mjx-end><mjx-c></mjx-c></mjx-end><mjx-mark></mjx-mark></mjx-stretchy-v></mjx-mo><mjx-mtable style="min-width: 9.776em;"><mjx-table><mjx-itable><mjx-mtr><mjx-mtd style="text-align: left; padding-right: 0.5em; padding-bottom: 0.1em;"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-tstrut></mjx-tstrut></mjx-mtd><mjx-mtd style="text-align: left; padding-left: 0.5em; padding-bottom: 0.1em;"><mjx-mtext class="mjx-n"><mjx-c class="mjx-c69"></mjx-c><mjx-c class="mjx-c66"></mjx-c><mjx-c class="mjx-c20"></mjx-c><mjx-c class="mjx-c6E"></mjx-c><mjx-c class="mjx-c20"></mjx-c><mjx-c class="mjx-c3D"></mjx-c><mjx-c class="mjx-c20"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c3B"></mjx-c></mjx-mtext><mjx-tstrut></mjx-tstrut></mjx-mtd></mjx-mtr><mjx-mtr><mjx-mtd style="text-align: left; padding-right: 0.5em; padding-top: 0.1em; padding-bottom: 0.1em;"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-tstrut></mjx-tstrut></mjx-mtd><mjx-mtd style="text-align: left; padding-left: 0.5em; padding-top: 0.1em; padding-bottom: 0.1em;"><mjx-mtext class="mjx-n"><mjx-c class="mjx-c69"></mjx-c><mjx-c class="mjx-c66"></mjx-c><mjx-c class="mjx-c20"></mjx-c><mjx-c class="mjx-c6E"></mjx-c><mjx-c class="mjx-c20"></mjx-c><mjx-c class="mjx-c3D"></mjx-c><mjx-c class="mjx-c20"></mjx-c><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c3B"></mjx-c></mjx-mtext><mjx-tstrut></mjx-tstrut></mjx-mtd></mjx-mtr><mjx-mtr><mjx-mtd style="text-align: left; padding-right: 0.5em; padding-top: 0.1em;"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D439 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.106em;"><mjx-texatom size="s" texclass="ORD"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2212"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-texatom></mjx-script></mjx-msub><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-c2B"></mjx-c></mjx-mo><mjx-msub space="3"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D439 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.106em;"><mjx-texatom size="s" texclass="ORD"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2212"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-texatom></mjx-script></mjx-msub><mjx-tstrut></mjx-tstrut></mjx-mtd><mjx-mtd style="text-align: left; padding-left: 0.5em; padding-top: 0.1em;"><mjx-mtext class="mjx-n"><mjx-c class="mjx-c69"></mjx-c><mjx-c class="mjx-c66"></mjx-c><mjx-c class="mjx-c20"></mjx-c><mjx-c class="mjx-c6E"></mjx-c><mjx-c class="mjx-c20"></mjx-c><mjx-c class="mjx-c3E"></mjx-c><mjx-c class="mjx-c20"></mjx-c><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c2E"></mjx-c></mjx-mtext><mjx-tstrut></mjx-tstrut></mjx-mtd></mjx-mtr></mjx-itable></mjx-table></mjx-mtable><mjx-mo class="mjx-n" style="vertical-align: 0.25em;"></mjx-mo></mjx-mrow></mjx-math><mjx-assistive-mml unselectable="on" display="block"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><msub><mi>F</mi><mi>n</mi></msub><mo>=</mo><mrow data-mjx-texclass="INNER"><mo data-mjx-texclass="OPEN">{</mo><mtable columnalign="left left" columnspacing="1em" rowspacing=".2em"><mtr><mtd><mn>0</mn></mtd><mtd><mtext>if n = 0;</mtext></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mtext>if n = 1;</mtext></mtd></mtr><mtr><mtd><msub><mi>F</mi><mrow data-mjx-texclass="ORD"><mi>n</mi><mo>−</mo><mn>1</mn></mrow></msub><mo>+</mo><msub><mi>F</mi><mrow data-mjx-texclass="ORD"><mi>n</mi><mo>−</mo><mn>2</mn></mrow></msub></mtd><mtd><mtext>if n > 1.</mtext></mtd></mtr></mtable><mo data-mjx-texclass="CLOSE" fence="true" stretchy="true" symmetric="true"></mo></mrow></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">\[F_n =  \begin{cases} 0  & \text{if n = 0;} \\ 1   & \text{if n = 1;} \\ F_{n-1} + F_{n-2}   & \text{if n > 1.} \end{cases}\]</span> </mjx-container></p>

<p>피보나치 수는 수학에서 위의 점화식으로 정의되는 수열이다. 피보나치 수는 0과 1로 시작하며, 다음 피보나치 수는 바로 앞의 두 피보나치 수의 합이 된다. n = 0, 1,...에 해당하는 피보나치 수는 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946… 이다. </p>

<p>프로그래밍 실습에서 문제 중 n을 입력 받았을 때 F<sub>n</sub>의 값을 출력하는 문제가 자주 등장한다. 실습을 하고 있던 희원이는 문득 이 문제가 너무 쉽다고 생각했다. 희원이는 실습 도중 반대로 F<sub>n</sub>이 주어졌을 때 n을 출력하는 문제는 어떨지 궁금했다.  피보나치 수 F<sub>n</sub>이 주어졌을 때 n을 출력하는 프로그램을 만들어 보자.</p>

### 입력 

 <p>첫 번째 줄에 테스트케이스를 나타내는 T(1 ≤ T ≤ 100)가 입력으로 주어진다. 두 번째 줄부터 각 테스트케이스마다 양의 정수 F<sub>n</sub>이 입력으로 주어진다. (1 ≤ F<sub>n</sub> ≤ 10<sup>21000</sup>, 1 ≤ N ≤ 100,000)</p>

### 출력 

 <p>피보나치 수 F<sub>n</sub>이 주어졌을 때 n을 출력한다. 만약 가능한 경우가 여러 개 있는 경우에는 가장 큰 인덱스를 출력하라. 피보나치 수가 아닌 수가 들어오는 경우는 없다.</p>

