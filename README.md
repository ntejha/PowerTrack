# PowerTrack

PowerTrack is a data-driven project aimed at monitoring and analyzing India's electricity sector. It aims to aggregate data from multiple authoritative sources to provide insights into generation, demand, emissions and policy impacts.

## How the project is going

 - [14-08-25] : Going to use mamba package manager because of its parallel downloading speed. Checkout how to use mamba in a basic level. [Link](Docs/Mamba.md).
 - [15-08-25] : Researched about the data sources, which can be used. These are the data sources, Check it out : [Link](Docs/Data.md). For scraping the CEA data, made a simple python script to the CEA data. when run the script it saves into two folder daily data and monthly data for CEA data only.
 - [16-08-25] : Thought of first consolidating the data of cea first, So, as of now importing and cleaning the data to usable format. As of now one done. Checkout the ipynb file for this [Notebook](src/transformations/cea_transformations.ipynb). Updated the data docs for better understanding.
 - [17-08-25] : Worked on the second file and cleaned it to a better format and restructured it to a good way. Thinking of first complete the cleaning of the daily generation and create a pipeline for the daily then jump to other data sources. You can see how i cleaned in the [Notebook](src/transformations/cea_transformations.ipynb).
 - [19-08-25] : Completed the Cleaning of data for the daily generation data.
