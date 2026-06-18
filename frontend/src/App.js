import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [taglines, setTaglines] = useState([]);

  useEffect(() => {
    fetch('/api/landing/taglines')
      .then(r => r.json())
      .then(d => setTaglines(d.taglines || []));
  }, []);

  const currentTagline = taglines.length > 0 ? taglines[0].text : 'Nothing could be better.';

  return (
    <div className="app">
      <header className="hero">
        <h1>Nothing Could Be Better</h1>
        <p className="subtitle">A dating site for nihilists</p>
        <p className="tagline">{currentTagline}</p>
        <p className="body">Find someone to stare into the void with. No algorithms, no ads, no meaning — just you and the abyss.</p>
        <nav className="nav-links">
          <a href="#profiles">Profiles</a>
          <a href="#forum">Forum</a>
          <a href="#matches">Matches</a>
          <a href="#gallery">Gallery</a>
        </nav>
      </header>
      <main className="content">
        <section id="profiles">
          <h2>Meet Others in the Void</h2>
          <p>Create your profile and find your match.</p>
        </section>
        <section id="forum">
          <h2>Forum</h2>
          <p>Share your existential musings.</p>
        </section>
        <section id="matches">
          <h2>Matching</h2>
          <p>Compatibility through shared nothingness.</p>
        </section>
        <section id="gallery">
          <h2>Gallery</h2>
          <p>Art of the void.</p>
        </section>
      </main>
      <footer>
        <p>Nothing Could Be Better — because nothing could actually be better.</p>
      </footer>
    </div>
  );
}

export default App;
