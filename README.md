<a href="www.covidconnect.co.in"><h1 id="covid-connect">Covid Connect</h1></a>
<p>A platform that connects help seekers with help providers around the world.</p>
<h2 id="why-covid-connect">Why Covid Connect?</h2>
<ul>
<li>Currently the major problem faced by the help seekers is that they are not able to connect to with the genuine help providers.</li>
<li>People are posting help needed on social platforms like Facebook, Twitter, Instagram but the reach on such platforms depends on post resharing and also if a genuine help provider found that post connecting with the original help seeker is still an issue because the reshared post is generally shared by the person who doesn’t know the help seeker.</li>
<li>Also If the help seeker changes his/her contact number, help providers cannot connect with him now as posts have the old number only.</li>
<li>So connecting help seekers with help providers is still a big issue that has to be  solved.</li>
</ul>
<h2 id="what-it-does">What it does?</h2>
<ul>
<li>On this platform a help seeker can add posts based on the category of help.</li>
<li>If the contact information of the help seeker is changed, then he/she can update his/her profile and details in all of his posts will be updated.</li>
<li>NGO’s can directly use it for connecting with various help seekers around the globe or in the local area.</li>
<li>Local Help providers can also connect with the authentic help seekers around there local area.</li>
<li>Covid Survivors can motivate others who are suffering and suggest them some tips on the testimonials page.</li>
<li>People can also directly donate to the “PM Help Care Fund” form the donate page.</li>
</ul>
<h2 id="tech-stack">Tech Stack</h2>
<ul>
<li>Backend: Django, Django REST Framework</li>
<li>Frontend: VueJS, Bulma CSS</li>
<li>Database: MongoDB Atlas</li>
</ul>
<h2 id="setting-up-locally">Setting up locally</h2>
<ul>
<li>Clone this repository.<br>
<code>git clone git@github.com:guptag911/Covid-Connect.git</code></li>
<li>Install NodeJS and set up npm or yarn.</li>
<li>Make a mongoDB Atlas account and make a database and get its database URL from connect menu.</li>
<li>Set enviroment variables ad COVIDDB = ‘URL’, where URL is MongoDB URL.</li>
<li>Now open up terminal  (For Frontend)<br>
<code>cd covidui</code><br>
<code>npm i</code></li>
<li>Open new terminal (For backend)<br>
<code>cd covidconnect</code><br>
pip install -r requirements.txt<br>
python <a href="http://manage.py">manage.py</a> makemigrations<br>
python <a href="http://manage.py">manage.py</a> migrate</li>
<li>This will install all dependencies into your local system.</li>
<li>Now open two terminal, in one type:</li>
<li><code>npm run serve</code></li>
<li><code>python manage.py runserver</code></li>
<li>You are all set up.</li>
</ul>


