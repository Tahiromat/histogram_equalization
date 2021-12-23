import streamlit as st
header = st.container()
intro = st.container()
process = st.container()
results = st.container()
more_about_eq = st.container()
conclusions = st.container()
referances = st.container()

with header:
    st.title('HISTOGRAM EQUALIZATION')
    st.markdown('Image processing is one of the rapidly growing technologies of our time and it has become an integral part of the engineering and computer science disciplines. Among its many subsets, techniques such as median filter, contrast stretching, histogram equalization, negative image transformation, and power-law transformation are considered to be the most prominent. In this tutorial, we will focus on the histogram equalization.')


with intro:
    st.subheader('What is a Histogram of An Image?')
    st.markdown("A histogram of an image is the graphical interpretation of the image’s pixel intensity values. It can be interpreted as the data structure that stores the frequencies of all the pixel intensity levels in the image.")
    st.image('data/im1.jpg')
    st.markdown("As we can see in the image above, the X-axis represents the pixel intensity levels of the image. The intensity level usually ranges from 0 to 255. For a gray-scale image, there is only one histogram, whereas an RGB colored image will have three 2-D histograms — one for each color. The Y-axis of the histogram indicates the frequency or the number of pixels that have specific intensity values.")
    st.image('data/im2.jpg')
    st.subheader("What is Histogram Equalization?")
    st.markdown("Histogram Equalization is an image processing technique that adjusts the contrast of an image by using its histogram. To enhance the image’s contrast, it spreads out the most frequent pixel intensity values or stretches out the intensity range of the image. By accomplishing this, histogram equalization allows the image’s areas with lower contrast to gain a higher contrast.")
    st.image('data/im3.jpg')
    st.subheader("Why Do You Use Histogram Equalization?")
    st.markdown("Histogram Equalization can be used when you have images that look washed out because they do not have sufficient contrast. In such photographs, the light and dark areas blend together creating a flatter image that lacks highlights and shadows. Let’s take a look at an example")
    st.image('data/Figure_1.png')
    st.markdown("In terms of Photography, this image is, without a doubt, a beautiful bokeh shot of a flower. However, for computer vision and image processing tasks, this photograph doesn’t provide much information since most of its areas are blurry due to lack of contrast.")
    st.markdown(
        "But not to be worried. We can use histogram equalization to overcome this problem. Let’s take a look!")


with process:
    st.subheader("How to Use Histogram Equalization")
    st.markdown("Before we get started, we need to import the OpenCV-Python package, a Python library that is designed to solve computer vision problems. In addition to OpenCV-Python, we will also import NumPy and Matplotlib to demonstrate the histogram equalization.")

    imports = '''
        import cv2 as cv
        import numpy as np
        from matplotlib import pyplot as plt'''
    st.code(imports, language='python')

    st.markdown(
        "Next, we will assign a variable to the location of an image and utilize .imread() method to read the image.")

    img_path = '''
        image_path = 'data/im4.jpg'
        test_image = cv.imread(image_path)
        test_image = cv.cvtColor(test_image,cv.COLOR_BGR2GRAY)
        '''

    st.code(img_path, language='python')

    st.markdown(
        "Then, we will use .imshow() method to view the image.The image will appear in a new window of your screen.")

    show_image = '''
        cv.imshow('image',img)'''
    st.code(show_image, language='python')


with results:
    st.markdown(
        "Now that our test image has been read, we can use the following code to view its histogram.")
    show_hist = '''
        hist,bins = np.histogram(test_image.flatten(),256,[0,256])
        cdf = hist.cumsum()
        cdf_normalized = cdf * float(hist.max()) / cdf.max()

        plt.plot(cdf_normalized, color = 'b')
        plt.hist(test_image.flatten(),256,[0,256], color = 'r')

        plt.xlim([0,256])
        plt.legend(('cdf','histogram'), loc = 'upper left')
        plt.show()'''
    st.code(show_hist, language='python')
    st.image('data/Output_1.png')

    st.markdown("As displayed in the histogram above, the majority of the pixel intensity ranges between 125 and 175, peaking around at 150. However, you can also see that the far left and right areas do not have any pixel intensity values. This reveals that our test image has poor contrast.")

    st.markdown("To fix this, we will utilize OpenCV-Python’s .equalizeHist() method to spreads out the pixel intensity values. We will assign the resulting image as the variable ‘equ’.")
    pix_intensity = '''
        equ_image = cv.equalizeHist(test_image)
        '''
    st.code(pix_intensity, language='python')

    st.markdown("Now, let’s view this image.")
    show_equ_img = '''
        equ_image = cv.equalizeHist(test_image)
        plt.imshow(equ_image)
        plt.show()'''
    st.code(show_equ_img, language='python')
    col1, col2 = st.columns(2)
    col1.image('data/Figure_1.png')
    col2.image('data/Figure_2.png')

    st.markdown("If you compare the two images above, you will find that the histogram equalized image has better contrast. It has areas that are darker as well as brighter than the original image.")

    st.markdown("Now, let’s compare the original and the equalized histograms. We will use the same code that we used to view the original histogram.")
    compare_hist = '''
        hist, bins = np.histogram(equ_image.flatten(), 256, [0, 256])
        cdf = hist.cumsum()
        cdf_normalized = cdf * float(hist.max()) / cdf.max()

        plt.plot(cdf_normalized, color='b')
        plt.hist(equ_image.flatten(), 256, [0, 256], color='r')

        plt.xlim([0, 256])
        plt.legend(('cdf', 'histogram'), loc='upper left')
        plt.show()
        '''
    st.code(compare_hist, language='python')
    col3, col4 = st.columns(2)
    col3.image('data/Output_1.png')
    col4.image('data/Output_2.png')

    st.markdown("Unlike the original histogram, the pixel intensity values now range from 0 to 255 on the X-axis. In a way, the original histogram has been stretched to the far ends. You may also notice that the cumulative distribution function (CDF) line is now linear as opposed to the original curved line.")


with more_about_eq:
    st.subheader("Adaptive Histogram Equalization (AHE)")
    st.markdown("Unlike ordinary histogram equalization, adaptive histogram equalization utilizes the adaptive method to compute several histograms, each corresponding to a distinct section of the image. Using these histograms, this technique spread the pixel intensity values of the image to improve the contrast. Thus, adaptive histogram equalization is better than the ordinary histogram equalization if you want to improve the local contrast and enhance the edges in specific regions of the image.")
    st.markdown(
        "One limitation of AHE is that it tends to overamplify the contrast in the near-contrast regions of the image.")

    st.subheader("Contrastive Limited Adaptive Equalization")
    st.markdown("Contrastive limited adaptive equalization (CLAHE) can be used instead of adaptive histogram equalization (AHE) to overcome its contrast overamplification problem. In CLAHE, the contrast implication is limited by clipping the histogram at a predefined value before computing the CDF. This clip limit depends on the normalization of the histogram or the size of the neighborhood region. The value between 3 and 4 is commonly used as the clip limit.")


with conclusions:
    st.subheader("Conclusion")
    st.markdown("Histogram equalization is a valuable image preprocessing technique that can be used to obtain extra data from images with poor contrast. With this technique, I hope you can improve the performances of your computer vision and machine learning tasks.")


with referances:
    st.subheader("References")
    st.markdown("(https://streamlit.io/)")
    st.markdown(
        "(https://levelup.gitconnected.com/introduction-to-histogram-equalization-for-digital-image-enhancement-420696db9e43)")
    st.markdown("(https://en.wikipedia.org/wiki/Histogram_equalization)")
    st.markdown("You can reach the source code from (https://github.com/Tahiromat/histogram_equalization)")
