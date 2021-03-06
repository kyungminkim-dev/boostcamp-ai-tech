## day12 학습정리

<br><br/>

### [AI Math 9강]

* Convolution 연산의 이해

    * 지금까지 배운 다층 신경망(MLP)은 각 뉴런들이 선형모델과 활성함수로 모두 연결된(fully connected) 구조였다. $h_i = \sigma(\sum_{j=1}^{p}{W_{ij}x_{j}})$ 각 성분 $h_i$에 해당하는 가중치 행 $W_i$이 필요하다.

    * Convolution 연산은 이와 달리 커널(kernel)을 입력벡터 상에서 움직여가면서 선형모델과 합성함수가 적용되는 구조이다. $h_i = \sigma(\sum_{j=1}^{k}{V_jx_{i+j-1}})$ 모든 $i$에 대해 적용되는 커널은 $V$로 같고 커널의 사이즈만큼 $x$상에서 이동하면서 적용합니다. 활성화 함수를 제외한 Convolution연산도 선형변환에 속합니다.

    * Convolition 연산의 수학적인 의미는 신호(signal)를 커널을 이용해 국소적으로 증폭 또는 감소시켜서 정보를 추출 또는 필터링하는 것이다.

    * continuous : $[f * g](x) = \int_{R^d}{f(z)g(x+z)dx} = \int_{R^d}{f(x+z)g(z)dx} = [g*f](x)$
    * discrete : $[f * g](i) = \sum_{a\in{z^d}}{f(a)g(i+a)} = \sum_{a\in{z^d}}{f(i+a)g(a)} = [g*f](i)$

    * 커널은 정의역 내에서 움직여도 변하지 않고(translation invariant) 주어진 신호에 국소적(local)으로 적용.

<br><br/>

* 다양한 차원에서의 Convolution 
    * Convolution 연산은 1차원뿐만 아니라 다양한 차원에서 계산이 가능

    * 1D-conv : $[f*g](i) = \sum_{p=1}^df(p)g(i+p)$

    * 2D-conv : $[f*g](i,j) = \sum_{p,q}f(p,q)g(i+p,j+q)$

    * 3D-conv : $[f*g](i,j,k) = \sum_{p,q,r}f(p,q,r)g(i+p,j+q,k+r)$

<br><br/>

* 2차원 Convolution 연산의 이해
    * 2D-Conv 연산은 이와 달리 커널을 입력벡터 상에서 움직여가면서 선형모델과 합성함수가 적용되는 구조이다.

    * 입력 크기를 $(H,W)$, 커널 크기를 $(K_H,K_W)$, 출력 크기를 $(O_H,O_W)$ 라 하면 출력 크기는 다음과 같이 계산한다. 

    $$O_H = H - K_H + 1$$
    $$O_W = W - K_W + 1$$

    * 채널이 여러개인 2차원 입력의 경우 2차원 Convolution을 채널 개수만큼 적용한다고 생각하면 된다.

    * 채널이 여러개인 경우 커널의 채널 수와 입력의 채널수가 같아야 한다.

    * 3차원부터는 행렬이 아닌 텐서라 부른다. 

    * 채널이 여러개인 2차원 입력의 경우 2차원 Convolution을 채널 개수만큼 적용한다고 생각하면 된다. 텐서를 직육면체 블록으로 이해하면 좀 더 이해하기 쉽다.

<br><br/>

* Convolution 연산의 역전파 이해
    * Convolution 연산은 커널이 모든 입력데이터에 공통으로 적용되기 때문에 역전파를 계산할 때도 convolution 연산이 나오게 된다.

    * ${\partial\over\partial x}[f*g](x) = {\partial\over\partial x}\int_{R^d}f(y)g(x-y)dy = \int_{R^d}f(y){\partial g\over\partial x}(x-y)dy = [f*g\prime](x)$

<br><br/>

### [DL Basic]

* Introduction 
    * Gradient Descent : First-order iterative optimization algorithm for finding a local minimum of a differentiable function.

<br><br/>

* Important Concepts in Optimization

    * Generalization : How well the learned model will behave on unseen data.

    * Under-fitting vs over-fitting

    * Cross validation (k-fold validation) : Cross-validation is a model validation technique for assessing how the model will generalize to an independent (test) data set.

    * Bias-variance tradeoff 
        * Given $D = {{\{(x_i,t_i)\}}_{i=1}^{N}}$ , where $t = f(x) + \epsilon \space and \space\epsilon \sim N(0,\sigma^2)$

        * We can derive that what we are minimizing (cost) can be decomposed into three different pars : $bias^2$, variance, and noise. 

        * variance 가 크면 overfitting 될 가능성이 크다. 

    * Bootstrapping
        * Boostrapping is any test or metric that uses random sampling with replacement.
    * Bagging and boosting

        * Bagging (Boostrapping aggregating)
            * Multiple models are being trained with boostrapping.

            * ex) Base classifiers are fitted on random subset where individual predictions are aggregated (voting or averaging).

        * Boosting

            * It focuses on those specific training samples that are hard to classify.

            * A strong model is built by combining weak learners in sequence where each learner learns from the mistakes of the previous weak learner.

    <br><br/>

* Gradient Descent Methods

    * Stochastic gradient descent
        * update with the gradient computed from a single sample.

    * Mini-batch gradient descent 
        * Update with the gradient computed from a subset of data.

    * Batch gradient descent
        * Update with the gradient computed from the whole data

    **Batch-size Matters**

        It has been observed in practice that when using a larger batch there is a degradation in the quality of the model, as measured by its ability to generalize.

        "We ... present numerical evidence that supports the view that large batch methods tend to converge to sharp minimizers of the training and testing functions. In contrast, small-batch methods consistently converge to flat minimizers... this is due to the inherent noise in the gradient estimation."
    
    

    1. Stochastic gradient descent  
    
        $W_{t+1} \longleftarrow W_{t} - \eta g_{t}$
    
    2. Momentum 

        $a_{t+1} \longleftarrow \beta a_{t}+g_{t}$
        
        $W_{t+1} \longleftarrow W_{t} - \eta a_{t+1}$

    3. Nesterov accelerated gradient

        $a_{t+1} \longleftarrow \beta a_{t} + \nabla\mathcal{}L(W_{t} - \eta \beta a_{t})$

        $W_{t+1} \longleftarrow W_{t} - \eta a_{t+1}$


    4. Adagrad
        * Adagrad adapts the learning rate, performing larger updates for infrequent and smaller updates for frequent parameters.

            $W_{t+1} \longleftarrow W_{t} - \frac{\eta}{\sqrt{G_{t} + \epsilon}}g_{t}$  ( $G_{t}$ : Sum of gradient squares,  $\epsilon$ : for numerical stability)

        * What will happen if the training occurs for a long period? 분모가 무한대로 가기때문에 $W$의 업데이트가 멈춤다.

        
    5. Adadelta
        * Adadelta extends Adagrad to reduce its monotonically decreasing the learning rate by restricting the accumulation window. 

        * There is no learning rate in Adadelta

            $G_{t} = \gamma G_{t-1} + (1 - \gamma)g_{t}^2$ 

            $W_{t+1} = W_{t} - \frac{\sqrt{H_{t-1} + \epsilon}}{\sqrt{G_{t}+ \epsilon}}g_{t}$

            $H_{t} = \gamma H_{t-1} + (1 - \gamma)(\Delta W_{t})^2$

            ($G_{t}$ : EMA of gardient squares, $H_{t}$ : EMA of different squares)

    6. RMSprop
        * RMSprop is an unpublished, adaptive learning rate method proposed by Geoff Hinton in his lecture.
        
            $G_{t} = \gamma G_{t-1} + (1 - \gamma)g_{t}^2$

            $W_{t+1} = W_{t} - \frac{\eta}{\sqrt{G_{t} + \epsilon}}g_{t}$  ($G_{t}$ : EMA of gradient squares, $\eta$ : stepsize)

    7. Adam
        * Adaptive Moment Estimation (Adam) leverages both past gradients squared gradients.

        * Adam effectively combines momentum with adaptive learning rate approach.

            $m_{t} = \beta_1m_{t-1} + (1 - \beta_1)g_{t}$

            $v_{t} = \beta v_{t-1} + (1 - \beta_2)g_t^2$

            $W_{t+1} = W_{t} - \frac{\eta}{\sqrt{v_t + \epsilon}} \frac{\sqrt{1 - \beta_2^t}}{1 - \beta_1^t}m_t$  ($m_t$ : Momentum, $v_t$ : EMA of gradient squares, $\eta$ : Stepsize)


<br></br>

* Regularization 

    * Early stopping

        * Note that we need additional validation data to do early stopping.

    * Parameter norm penalty

        * It adds smoothness to the function space.

            $total cost = loss(D;W) + \frac{\alpha}{2} \rVert W \rVert^2_2$

            ($\frac{\alpha}{2} \rVert W \rVert^2_2$ : Parameter Norm Penalty)

    * Data augmentation

        * More data are always welcomed. 

        * However, in most cases, training data are given in advance.

        * In such cases, we need data augmentation.

    * Noise robustness

        * Add random noises inputs or weights.

    * Label smoothing

        * Mix-up constructs augmented training examples by mixing both input and output of two randomly selected training data. 

        * CutMix constructs augmented training examples by mixing inputs with cut and paste and outputs with soft labels of two ranomly selected training data.

    * Droupout

        * In each forward pass, randomly set some neurons to zero.

    * Batch normalization

        * Batch normalization compute the empirical mean and variance independently for each dimension (layers) and normalize.

            $\mu_B = \frac{1}{m}\sum_{i=1}^{m}x_{i}$

            $\sigma^2_B = \frac{1}{m}\sum_{i=1}^{m}(x_{i} - \mu_B)^2$

            $\hat x_{i} = \frac{x_{t}-\mu_B}{\sqrt{\sigma^2_B + \epsilon}}$

    
    








    









