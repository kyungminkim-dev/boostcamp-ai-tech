## day11 학습정리 

* 베이즈 통계학 

    * 베이즈 통계학은 하나의 사건에서의 믿음의 정도를 확률로 나타내는 베이즈 확률론에 기반한 통계학 이론이다. 믿음의 정도는 이전 실 험에 대한 사전 지식에 기반할 수 있다.

    * 베이즈 통계학을 이해하기 위해서는 조건부 확률의 개념을 이해해야 한다. 

    * 베이즈 정리는 조건부확률을 이용하여 정보를 갱신하는 방법을 알려준다.

    * A라는 새로운 정보가 주어졌을 때 P(B)로 부터 P(B|A)를 계산하는 방법을 제공한다. 

    * COVID-19 의 발병률이 10%로 알려져있다. COVID-19에 실제로 걸렸을때 검진될 확률은 99%이고 실제로 걸리지 않았을 때 오진될 확률이 1%라고 할 때, 어떤 사람이 질병에 걸렸다고 검진결과가 나왔을 때 정말로 COVID-19에 감염되었을 확률은? 

    * 오탐율이 오르면 테스트의 정밀도가 떨어진다.

    * 베이즈 정리를 통해 새로운 데이터가 들어왔을 때 앞서 계산한 사후확률을 사전확률로 사용하여 갱신된 사후확률을 계산할 수 있다. 

    * 앞서 COVID-19 판정을 받은 사람이 두 번째 검진을 받았을 때도 양성이 나왔을 때 진짜 COVID-19에 걸렸을 확률은?

* 조건부 확률 -> 인과관계?

    * 조건부 확률은 유용한 통계적 해석을 제공하지만 인과관계(causality)를 추론할 때 함부로 사용해서는 안된다.

    * 데이터가 많아져도 조건부 확률만 가지고 인과관계를 추론하는 것을 불가능 하다.

    * 인과관계는 데이터 분포의 변화에 강건한 예측모형을 만들 때 필요하다. 

    * 인과관계를 알아내기 위해서는 중첩요인의 효과를 제거하고 원인에 해당하는 변수만의 인과관계를 계산해야 한다. 

<br><br/>

* 딥러닝_기본_용어설명

    * Key Components of Deep Learning

        <ol>
        <li>The data that the model can learn from</li>
        <li>The model how to transform the data</li>
        <li>The loss function that quantifies the badness of the model</li>
        <li>The algorithm to adjust the parameters ro minimize the loss</li>
        </ol>

    * Data 
        * Data depend on the type of the problem to solve. (Classification, Semantic Segmentation, Detection, Pose Estimation, Visual QnA)

    * Model 
        * AlexNet, GoogLeNet, LSTM, Deep AutoEncoders, GAN etc.

    * Loss
        * The loss function is a proxy of what we want to achieve
            * Regression Task : MSE(Mean square error)
            * Classification Task : CE(cross enthropy)
            * Probabilistic Task : MLE

    * Optimization Algorithm
        * SGD
        * Momentum
        * NAG
        * Adagrad
        * Adadelta
        * Rmsprop

        모델이 학습데이터뿐만 아니라 한번도 보지못한 데이터에 또는 실 환경에서 잘 동작하는 것을 목표로 하여 다음과 같은 알고리즘을 추가함 

        * Dropout
        * Early stopping 
        * k-fold validation
        * Weight decay
        * Batch normalization
        * MixUp
        * Ensemble
        * Bayesian Optimization
    
* Historical Review

    * <p>Denny Britz 블로그<a href="www.naver.com"></a>를 참조</p> 

    * 2012 - AlexNet(CNN)
        * 224 by 224의 이미지가 들어왔을 때 이를 분류 
        * 처음으로 딥러닝이 ImageNet Large Scale Visul Recognition Challenge에서 우승. 
        
    * 2013 - DQN
    * 2014 - Encoder / Decoder, Adam Optimizer
    * 2015 - GAN(Generative Adversarial Network), ResNet(Residual Networks)
    * 2017 - Transformer(Attention Is All You Need)
    * 2018 - BERT(fine-tuned NLP models)
        * Bidirectional Encoder Representations from Transformers
    * 2019 - BIG Language Models(GPT-X)
        * GPT-3, an autoregressive language model with 175 billion parameters
    * 2020 - Self-Supervised Learning
        * SimCLR : a simple framework for contrastive learning of visual representation


<br><br/>

* PyTorch
    * Numpy + AutoGrad + Function
    * Numpy구조를 가지는 Tensor 객체로 array 표현 
    * 자동미분을 지원하여 DL 연산을 지원
    * 다양한 형태의 DL을 지원하는 함수와 모델을 지원함
        

<br><br/>

* Neural Networks 
    * Neural networks are computing systems vaguely inspired by the biological neural networks that constitute animal brains.
    * Neural networks are function approximators that stack affine transformation followed by nonlinear transformations.
    * Linear Neural Networks
        * 입력과 출력이 1차원 
        * Data : 
        * Model : 
        * Loss : 

        * of course, we can handle multi dimensional input and ouput.
            * y = W^Tx + b
            * One way of interpreting a matrix is to regard it as a mapping between two vector spaces.
    * Beyond Linear Neural Networks
        * What if we stack more?
            * y = W2^Th = (W2^TW1^T)x  : Another matrix 의미가 없다.
            * y = W2^Th = W2^TP(W1^Tx) : Nonlinear transform (activate function)
        * Activation functions 
            * Rectified Linear Unit(ReLU)
            * Sigmoid 
            * Hyperbolic Tangent
    * Multi-Layer Perceptron
        * This class of architectures are often called multi-layer perceptrons.
        * of course, it can go deeper.
        * What about the loss functions?
            * Regression Task : MSE
            * Classification Task : CE
            * Probabilistic Task = MLE

    
    

