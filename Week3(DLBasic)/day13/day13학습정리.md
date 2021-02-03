### day13 학습정리 

* Convolution 

    * Continuous convolution

        $(f*g)(t) = \int f(\tau)g(t-\tau)d\tau = \int f(t-\tau)g(t)d\tau$

    * Discrete convolution
    
        $(f*g)(t) = \sum_{i=- \infty}^{\infty}f(i)g(t-i) = \sum_{i=- \infty}^{\infty}f(t-i)g(i)$

    * 2D image convolution

        $(I*K)(i,j) = \sum_{m}\sum_{n}I(m,n)K(i-m,j-n) = \sum_{m}\sum_{n}I(i-m,i-n)K(m,n)$

* Convolutional Neural Networks

    * CNN consists of convolution layer, pooling layer, and fully connected layer.

    * Convolution and pooling layers : feature extraction

        * 합성곱 신경망에서는 풀링 층을 사용해 표현의 크기를 줄임으로써 계산속도를 줄이고 특징을 더 잘 검출 해낼 수 있다.

        * parameter를 줄이기 때문에, 해당 network의 표현력이 줄어들어 overfitting을 억제.

        * max pooling, avg pooling 두가지 종류가 있다. 보통 max pooling을 사용 


    * Fully connected layer : decision making (e.g., classification)

        * 완전연결 계층은 한 층의 모든 뉴런이 다음 층의 모든 뉴런과 연결된 상태를 이야기 한다. 


* Alexnet

    * Key ideas

        * Rectified Linear Unit (ReLU) activation

        * GPI implementation(2 GPUs) : 병렬적 구조

        * Local response normalization, Overlapping pooling

        * Data augmentaion

        * Dropout

    * ReLU Activation

        * preseves properties of linear models

        * Easy to optimize with gradient descent

        * Good generalization

        * Overcome the vanishing gradient problem

* VGGNet

    * Increasing depth with 3 * 3 convolution filters(with stride 1)

    * 1 * 1 convolution for fully connected layers

    * Dropout (p=0.5)

    * VGG16, VGG19

    * Why 3 * 3 convolution ?  ==> 

* GoogLeNet

    * GoogLeNet won the ILSVRC at 2014 (It combined network-in-network(NiN) with inception blocks.)

        **Inception Block**
        
            What are the benefits of the inception block? ==> Reduce the number of parameter.

            How to reduce paramters? 

            1. Recall how the number of parameters is computed.

            2. 1 X 1 convolution can be seen as channel-wise dimension reduction.

            Benefit of 1X1 convolution : 1X1 convolution enables about 30% reduce of the number of parameters!

* ResNet

* DenseNet


            
        
    




    
