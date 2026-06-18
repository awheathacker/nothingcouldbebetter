import React from 'react';

function Navbar() {
  const links = [
    { label: 'Home', href: '/' },
    { label: 'Profiles', href: '/profiles' },
    { label: 'Matches', href: '/matches' },
    { label: 'Forum', href: '/forum' },
    { label: 'About', href: '/about' },
  ];

  return (
    <nav className="navbar">
      <div className="navbar-brand">
        <a href="/">Nothing<span>CouldBeBetter</span></a>
      </div>
      <ul className="navbar-links">
        {links.map(l => (
          <li key={l.label}>
            <a href={l.href}>{l.label}</a>
          </li>
        ))}
      </ul>
    </nav>
  );
}

export default Navbar;
