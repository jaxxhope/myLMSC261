# Creating a Solar System in GlowScript
 # https://www.youtube.com/watch?v=p4dHfQuNUrE
# Starting Out
-
- I started out with this particular youtube video listed above. The youtube video before a piece of code to get you started on this solar system creation journey. I did not realize that this video was essentially a challenge. It presented a piece of starter code to get one started on the project and then proceed with the process by figuring out further code to add more planets and even possibly make alterations to the code as well as the dimensions of the planets.

# Understanding the Code
- While creating this project I searched the web for code that would help me complete this project, or help me better understand the assessment. With time I realized that this project would be one that would require and make sense for me to grasp a better understanding of, it wasn't just about finding code that works and runs well, which I found and it's exactly what I wanted, but I wanted to understand why the code ran so well and what went into the process of creating such code like so, and that's the direction my project ended up going into. There is a finished project, code that I've discovered online, although the biggest takeaway from this project was understanding and breaking down the code as well as logistics behind it, which gives me insight into how these things work as well as how to go about approaching future projects similar to this, which I feel is the best takeaway.

# So How Does It All Work? Understanding the setup
- To understand the code behind my project I needed to understand how Gravity and Orbits work in GlowScript.
- I followed and read through this article for guidance. https://www.wired.com/2015/03/glowscript-tutorial-8-gravity-orbits/
- By Reading this article I discovered that If there are two objects with mass there is a gravitational force that pulls them together
- graphic
- mass 1 pulls on mass 2 with the same force that 2 pulls on 1, because they are the same force, vector r is from mass 1 to mass to.
- graphic
- The Article also listed a formula for the gravitational force on the moon:
- Fg=-G*Earth.m*moon.m*r/mag(r)**3
- This formula also always viewers to see how the Earth and moon scale are the correct distance and makes it move, it keeps calculating the gravitational force of the moon. "r" is represented as the distance from the earth to the moon.
- The article also explains how you have to consider the time step which is the "incremental change in time for which the governing equations are being solved" https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjHhISCwbfwAhXRKs0KHRrfDKIQFjABegQIAxAD&url=https%3A%2F%2Fwww.researchgate.net%2Fpost%2FWhat_is_the_meaning_of_time_steps_in_Ansys_130&usg=AOvVaw3aIC8217tEaFH2sQ0e4l23
- it gave an example of code that could be used to create a loop an act as a time step
- Since the moon does not crash into the earth and instead orbits the earth the is an initial momentum of the moon that has to be established
- As the moon moves in a circle there is centripetal acceleration, which is an object moving in uniform circular motion (https://www.khanacademy.org/science/physics/centripetal-force-and-gravitation/centripetal-acceleration-tutoria/a/what-is-centripetal-acceleration)
- Knowing the mass of the Earth the radius of the circulation motion you can then put in your b\values to get the velocity.
- For the initial velocity the moon starts on the x-axis so it has to be moving in the y-axis direction
- Through my meeting with Rachel I learned that the coordinates (x,y,z) x is going up, y is going across, and z is pointing down in the context of a GlowScript IDE.
- There are also other things to consider such as how long does it take for each planet to fully orbit around the sun. This is what I found :
- Mercury: 88 days
- Venus : 225 days
- Earth: 365 days
- Mars: 687 days
- Jupiter: 4,333 days
- Saturn: 10,756 days
- Uranus: 30,687 days
- Neptune: 60,190 days

# In the Context of The Code I Discovered
- In order to simulate the solar system you first have the find the mass, orbital velocity, radius, and initial momentum of the earth as well as the distance of the earth from the sun
- Then have to figure out the coordinates for each planet, the radius as well as the coloring for appearing
- After that is completed those initial velocities must be added in, initial velocities for each individual planet
- Then trails that'll trail behind each planet to track its orbit will need to be created as well as arrows
- Once that is done the planets gravitational forces must be added in as well as their position and individual trails and arrows and this works by the use of if else statements
# In Conclusion
- With the code I used which was from https://github.com/owendix/glowscript.org-VPython-Code/blob/master/solarSystemMotion.py all of the information I gathered was seen in this example
- The Result: https://www.glowscript.org/#/user/jhope2/folder/MyPrograms/program/3DSolarSystemtest3
- This project allowed me to learn allowed about planets and translating information about how they work in a real life solar system into a digital solar System
- I also learned more about inserting information like so as well as understanding code which was my goal for this entire project, I feel that throughout this semester I've used code given to me by Rachel and the code works, functions, and runs perfectly but I haven't quite understood why and how. Breaking down this project and building upon the basics of it allowed me to fully understand the use of the code which helps me overall understand how to be a more informed coder and furthers my understanding of how code works, I'm grateful for the opportunity to do so. 
