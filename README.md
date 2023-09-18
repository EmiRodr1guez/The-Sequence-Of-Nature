# The-Sequence-Of-Nature
A web based application that analyses the frequency data (Hz) of a desired/uploaded song and tells you what it is.
<br>
<br>
## Technologies being used to develop this Web-application
<ul>HTML</ul>
<ul>CSS</ul>
<ul>JavaScript</ul>
<ul>Bootstrap</ul>
<ul>Python (Data Processing and Analysis)</ul>
<ul>Flask (Back-end engine)</ul>
<ul>Jinja2 (HTML templating engine)</ul>

## What we've learned with this project
Before this project began a great inspiration 
for the love for music was taken for this project, 
the passion for music was the essence of this project.
<br>
<br>
With this deep inspiration, the desire to learn an array 
of concepts from Digital Signal Processing and Audio 
Engineering, was born. We soon realized that in order to 
be successful in this project we must understand concepts 
of Digital Signal Processing and Audio Engineering like; 
Fast Fourier Transform, Time Domain, Frequency Domain, 
Dual Channel, Frequency Bins, Hertz, Musical Notes, WAV files, 
and Pitch, just to name a few.

### Ruben's notes:

With a basic understanding of these concepts we grasped the ability 
to build Sequence of Nature.
<br>
<br>
1. We discovered that in order to find the frequency of a song a WAV file 
had to be fed into the program.
<br>
<br>
2. Once the WAV file was extracted, the data within the file was then 
transformed using the exuberant algorithm: Fast Fourier Transform 
using the SciPy module.
<br>
<br>
3. This mathematical algorithm gave us the ability to transform audio 
data from the Time Domain into the Frequency Domain. Where the algorithm 
would return an array of Frequency Bins.
<br>
<br>
4. Given this array of Frequency Bins, we had the data to begin 
an analysis among the frequencies played in the song.
<br>
<br>
5. Understanding that within each song there is a collection of instruments 
playing their own series of notes, and considering that each note played 
by each instrument in the song has its own frequency, within the array of 
frequency bins there is an absolute vast amount of data to be analyzed.
<br>
<br>
6. Considering this observation and considering the limited computational 
resources in scalability we had to improvise.
<br>
<br>
7. We decided that analyzing the most dominant frequencies in the song by how 
often they are played (not by how loud they are, since that does not determine 
the frequency of a note, that is Pitch) would be enough to calculate a reasonable 
frequency from a given song.
<br>
<br>
NOTE: although it is possible to consider all notes from a given song, this method 
of analysis would be more adequate with a Machine Learning model who is trained to 
detect musical notes and process all through a Neural Network.
<br>
<br>
8. Final observations along with their cons/drawbacks:<br> 
8.1.Data in the WAV file is extremely sensitive, meaning the farther away it is from 
“Production” quality, the analysis will be inaccurate.<br>
8.2.Longer songs over 30seconds is extremely hard to process since the amount of data 
is so big, it causes a scalability issue and can cause the computer to crash, or simply 
return 0.0 to prevent system failure.
<br>
<br>
9. Implementing a Machine Learning Model for more accurate frequency analysis and scaling 
data through Neural Networks would definitely expand and enchant the quality of this web-app 
until then, Sequence of Nature is yet to experience its metamorphosis.
