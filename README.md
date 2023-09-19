# The Sequence Of Nature 🎶
A web-based application that analyzes the frequency data (Hz) of a desired/uploaded song and tells you what it is. 

## Technologies Being Used to Develop This Web-Application 🛠️
- HTML
- CSS
- JavaScript
- Bootstrap
- Python (Data Processing and Analysis)
- Flask (Back-end engine)
- Jinja2 (HTML templating engine)

## What We've Learned With This Project 📚
Before this project began, a great inspiration for the love for music was taken for this project, the passion for music was the essence of this project. 

With this deep inspiration, the desire to learn an array of concepts from Digital Signal Processing and Audio Engineering was born. We soon realized that in order to be successful in this project, we must understand concepts of Digital Signal Processing and Audio Engineering like Fast Fourier Transform, Time Domain, Frequency Domain, Dual Channel, Frequency Bins, Hertz, Musical Notes, WAV files, and Pitch, just to name a few.


### Ruben's notes:

With a basic understanding of these concepts we grasped the ability 
to build Sequence of Nature.
<br>
<br>
1.We discovered that in order to find the frequency of a song a WAV file 
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
of analysis would be more adequate with a Machine Learning model that is trained to 
detect musical notes and process them all through a Neural Network.
<br>
<br>
8. Final observations along with their cons/drawbacks:<br> 
8.1. Data in the WAV file is extremely sensitive, meaning the farther away it is from 
“Production” quality, the analysis will be inaccurate.<br>
8.2. Longer songs over 30seconds is extremely hard to process since the amount of data 
is so big, it causes a scalability issue and can cause the computer to crash, or simply 
return 0.0 to prevent system failure.
<br>
<br>
9. Implementing a Machine Learning Model for more accurate frequency analysis and scaling 
data through Neural Networks would definitely expand and enchant the quality of this web-app 
until then, Sequence of Nature has yet to experience its metamorphosis.

## <h1> Emiliano's notes: </h1>

## :gear: Efficient Data Conversion

Our journey began by tackling the challenge of efficiently converting audio files into raw data suitable for analysis. We quickly recognized the power of WAV files in this regard. These files come pre-packaged with parsed sound wave data, making them an invaluable resource for our project.

## :chart_with_upwards_trend: Optimizing for File Size

One of the pivotal hurdles we encountered was managing file sizes. WAV files contain a wealth of information, including intricate details about sound waves, encodings, and containers. For instance, processing an entire 2-minute song would trigger data overflow, resulting in a graceful program exit but an unexpected dominant wavelength of 0.0. Our solution? Precision trimming. By isolating just 5 seconds of audio, we achieved flawless and efficient display of the dominant frequency.

## :art: Elegance of Jinja Templating

A crucial revelation was the elegance and stability offered by Jinja templating. Instead of resorting to repetitive copy-paste styling, we harnessed the power of templates. This approach ensured clean and maintainable code. With templates in place, the addition of new features or pages became a simple, one-step process. We employed headers for the core design framework and footers for essential footer information, keeping these elements static for a streamlined user experience.

## :art: Harnessing Bootstrap for Consistency

An essential cornerstone of our front-end development strategy was the adoption of Bootstrap. This powerful framework played a pivotal role in maintaining a consistent and visually appealing design throughout the entire program. In a world where disorganized styling can detract from user experiences, Bootstrap's wealth of components and features empowered us to deliver a polished and cohesive interface.

## :link: Seamless Backend-Frontend Integration with Flask

The backbone of our project's integration between the backend and frontend was Flask. Every time a user submitted a song, Flask facilitated the smooth transmission of data and executed the method responsible for parsing and returning the dominant frequency. This robust framework ensured a seamless and responsive user experience, transforming song submissions into actionable results with precision and efficiency.

## :inbox_tray: File Upload Handling

Efficient file upload handling is at the core of our user experience. Our Bootstrap-designed HTML form ensures an appealing and responsive layout. Users can easily select and upload WAV files with enforced WAV file selection through the "accept" attribute. On submission, the form triggers a POST request, seamlessly integrating our front-end with the Flask backend. The "required" attribute guarantees complete submissions, enhancing overall application reliability and user-friendliness.

## :electric_plug: External Script Inclusion

Our project thrives on the seamless integration of critical external scripts, boosting interactivity and dynamism. We strategically incorporate jQuery from the official CDN, simplifying DOM manipulation and event handling for a responsive interface. Popper.js, sourced from a CDN, smooths Bootstrap's popovers and tooltips, offering users valuable insights. Bootstrap's JavaScript components, fetched from a CDN, extend our design framework, enabling modals, dropdowns, and responsive navigation. This thoughtful integration enriches our application, elevating engagement and usability while preserving efficient and organized code.
