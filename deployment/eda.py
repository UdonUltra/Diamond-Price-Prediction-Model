import streamlit as st
from PIL import Image

def app():
    st.title('EDA')
    
    # EDA 1
    st.write('1. How is the frequency of Cut Quality from this dataset?')
    image = Image.open('eda_1.png')
    st.image(image)
    st.write('From Cut we can see that 3% of diamond in this datasets are having fair cut, while Ideal cut has highest count compared to all categories with 40% from total percentage. This implies that most of dataset have above standard cut quality with lower quality only on fair improvement because the lowest cut quality category in here are Fair, and it is the lowest count percentage overall.')

    # EDA 2
    st.write('2. How is the frequency of Color Quality from this dataset?')
    image = Image.open('eda_2.png')
    st.image(image)
    st.write("From Color category, we can see that J category has lowest count. This also are the lowest quality from this set. This imply that only small fraction of diamond dataset has low quality. Rest of color quality category aren't significantly different in terms of percentage.")
    st.write("G color, which is the highest quality color for near colorless Diamond are the highest count with 20.9% percents count. But colorless color quality which is higher quality such F, E, and D have small percentage difference compared to G, meaning that many diamonds in this dataset has generally good quality in term of color.")

    # EDA 3
    st.write('3. How is the frequency of Clarity Quality from this dataset?')
    image = Image.open('eda_3.png')
    st.image(image)
    st.write("There are only small amount of diamonds that have l1, which is one of worst quality because of how inclusions are visible by naked eyes. IF and VVS1 which is having the best clarity quality, also has lower amount in this plot.")
    st.write("SI1 has the highest percentage on pie chart with 24.2%, followed by VS2 with 22.7%, SI2, and VS1. These clarity grades are mid level grade, implying that many diamonds in this dataset are having mid level grade. This is logical as high clarity diamonds are rare, and most of diamonds with these mid level grade clarity are good enough since people won't notice inclusions in these grades with naked eyes.")

    # EDA 4
    st.write('4. How is the frequency of Carat Quality from this dataset?')
    image = Image.open('eda_4.png')
    st.image(image)
    st.write("From Carat value distribution plot, we can see that datas are highly distributed around 0.30 carat to 1.0 carats. This implies that most of diamonds in this data are light weighted since carat represents weight of the diamond itself.")

    # EDA 5
    st.write('5. What is Distribution of Diamond Width?')
    image = Image.open('eda_5.png')
    st.image(image)
    st.write("From this plot, we can see that distribution of depth percentage are around 61% to 63%. which an ideal depth percentage on some diamond shape. This implies that many diamonds in this dataset have less low-quality diamonds that aren't cut well.")

    # EDA 6
    st.write('6. What is Distribution of Diamond Table?')
    image = Image.open('eda_6.png')
    st.image(image)
    st.write("Most of diamonds in this database are highly distributed around 55% to 60% percents. Diamonds that is falling into this categories usually having ideal Table percentage. From this plot and insights from depth percentage distribution, we can see that most of diamonds in this dataset are cutted well, which results in good brilliance.")

    # EDA 7
    st.write('7. How are Length, Width, and Depth influence pricing?')
    image = Image.open('eda_7.png')
    st.image(image)
    st.write("There is a positive correlation between Length and Price, which as Diamond lenght increased, so the price. But the relationship is not perfectly linear, as the data points are not perfecly clustered on straight line, but a rather curved one. This suggests that the length increase, the price are increasing at steeper angle, which means that the price are become more expensive and increasingly valuable.")
    st.write("For Width and Depth, the relation with price seems similiar with length plot. There is positive correlation where as width and depth increase, so the price. But the relationship is not perfectly linear. The acceleration of price increase as width and depth increase are also higher than Length to Price relationship. This suggests that small increase in Depth and Width will highly increase pricing in general.")

    # EDA 8
    st.write('8. How is Relation of Carat to Price?')
    image = Image.open('eda_8.png')
    st.image(image)
    st.write("There are positive correlation between diamond carat to its price, where as carat increase, so the price.")
    st.write("The relation is not linear because many data points doesn't form a perfect line, but rather a curved one. This indicates that in general as carat increase, the price increased rapidly.")
    st.write("Some data points are highly clustered on 1 and approximately 1.5 and 2 carat with wide variety of price. This suggests that diamonds are desirable in this seems standardized carat weight, which is a lightweight diamonds that may be vary from lower price to higher price that might depends on other 4C factor(Clarity, Cut, Color) and also its size.")
    st.write("In this plot we can see several outliers that has extremely high carats with narrow to no variety of price, particularly on higher side of price. This suggests that extremely high carat diamonds can be considered a product with high prestige value.")


    # EDA 9
    st.write('9. How is the frequency of Clarity Quality from this dataset?')
    image = Image.open('eda_9.png')
    st.image(image)
    st.write("On color quality, J color is having higher price median compared to any color quality, even though J is the lower quality in near colorless category. On the other hand, D (absolutely colorless) which is the highest quality in diamond color, are second lowest price median. This suggests that customer doesn't see higher quality color as sole determinator for setting the price.")
    st.write("On cut quality, Fair has highest price median, while Ideal which is the highest cut quality, has lowest price median. On the other hand, Premium which is second highest quality cut, has wider range of price variety. This implies that diamonds market has more demand on Fair cut and Premium cut compared to Ideal cut, assuming that fair and premium cut are more accessible compared to ideal, and also other factor might also influence price.")
    st.write("On clarity, we can see that SI2 has higher median on price compared to other clarity classification. SI2 are second lowest clarity quality, before l1, which also have higher median on price. This implies that clarity also cannot become a sole determinator for setting the price.")

    