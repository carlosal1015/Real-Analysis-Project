import matplotlib.pyplot as plt

def plot(self, f, stepSize=0.01, discreteStyle='b.', intervalStyle='r-', **kwargs):
    """
    Plotting functionality.
    
    Required argument:
    	f: The function that will determine the y values of the graph - the x values are determined by the current timescale values.

	Optional arguments:
    	stepSize: The accuracy to which the intervals are drawn in the graph - the smaller the value, the higher the accuracy and overhead.
    	discreteStyle, intervalStyle: These arguments determine the color, marker, and line styles of the graph.
    	They accept string arguments of 3-part character combinations that represent a color, marker style, and line style.
    	For instance the string "-r." indicates that the current (x, y) points should be plotted with a connected line
    	(represented by the "-"), in a red color (represented by the "r"), and with a point marker (represented by the ".").
    	These character combinations can be in any order UNLESS the reordering changes the interpretation of the character combination.
    	For instance, the string "r-." does not produce the same result as the string "-r.".
    	This is because "-." indicates a "dash-dot line style" and is therefore no longer interpreted as a "point marker" with a "solid line style".
    	See the notes section of this resource for more information: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html

    	**kwargs:
    	This argument gives the user access to all the arguments of the matplotlib.pyplot.plot function (this includes markersize, linewidth, color, label, and dashes).
    	For a list of all available parameters, see: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html

    NOTE: To display plots that are created with this function, call the show() function of the plt data member of this class.
    """
    xDiscretePoints = []
    yDiscretePoints = []

    intervals = []

    for tsItem in self.ts:
        if isinstance(tsItem, list):
            xIntervalPoints = []
            yIntervalPoints = []

            for intervalValue in np.arange(tsItem[0], tsItem[1], stepSize):
                xIntervalPoints.append(intervalValue)
                yIntervalPoints.append(f(intervalValue))

            xyIntervalPointsPair = [xIntervalPoints, yIntervalPoints]

            intervals.append(xyIntervalPointsPair)

        else:
            xDiscretePoints.append(tsItem)
            yDiscretePoints.append(f(tsItem))

    plt.plot(xDiscretePoints, yDiscretePoints, discreteStyle, **kwargs)    
    
    labeled = False
    removedLabel = False

    if "label" in kwargs:
        if discreteStyle == intervalStyle:            
            kwargs.pop("label")
            removedLabel = True       

    for xyIntervalPointsPair in intervals:
        if "label" in kwargs:
            if labeled == True and removedLabel == False:                
                kwargs.pop("label")    
                removedLabel = True                  
            
        plt.plot(xyIntervalPointsPair[0], xyIntervalPointsPair[1], intervalStyle, **kwargs)
        
        labeled = True

def scatter(self, f, stepSize=0.01, **kwargs):
    """
    Scatter plotting functionality.
    
    Required argument:
    f: The function that will determine the y values of the graph - the x values are determined by the current timescale values.

	Optional arguments:
    stepSize: The accuracy to which the intervals are drawn in the graph - the smaller the value, the higher the accuracy and overhead.

    **kwargs: This argument gives the user access to all the arguments of the matplotlib.pyplot.scatter function (this includes marker, color, and label).
    
	For a list of all available parameters, see: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.scatter.html
    
    NOTE: To display plots that are created with this function, call the show() function of the plt data member of this class.
    """
    xDiscretePoints = []
    yDiscretePoints = []

    intervals = []

    for tsItem in self.ts:
        if isinstance(tsItem, list):
            xIntervalPoints = []
            yIntervalPoints = []

            for intervalValue in np.arange(tsItem[0], tsItem[1], stepSize):
                xIntervalPoints.append(intervalValue)
                yIntervalPoints.append(f(intervalValue))

            xyIntervalPointsPair = [xIntervalPoints, yIntervalPoints]

            intervals.append(xyIntervalPointsPair)

        else:
            xDiscretePoints.append(tsItem)
            yDiscretePoints.append(f(tsItem))
        
    plt.scatter(xDiscretePoints, yDiscretePoints, **kwargs)    

    if "label" in kwargs:
        if "color" in kwargs:
            kwargs.pop("label")
            
    for xyIntervalPointsPair in intervals:            
        plt.scatter(xyIntervalPointsPair[0], xyIntervalPointsPair[1], **kwargs)