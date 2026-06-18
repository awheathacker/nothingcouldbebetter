import React, { useEffect, useState } from 'react';

function fetchJSON(path, opts = {}) {
  const base = '/api';
  return fetch(`${base}${path}`, opts).then(r => {
    if (!r.ok) throw new Error(`HTTP ${r.status}: ${r.statusText}`);
    return r.json();
  });
}

export function useTaglines() {
  const [taglines, setTaglines] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchJSON('/landing/taglines').then(setTaglines).finally(() => setLoading(false));
  }, []);

  return { taglines, loading };
}

export function useHero() {
  const [hero, setHero] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchJSON('/landing/hero').then(setHero).finally(() => setLoading(false));
  }, []);

  return { hero, loading };
}

export function useProfiles() {
  const [profiles, setProfiles] = useState([]);
  const [loading, setLoading] = useState(true);

  const refresh = () => {
    setLoading(true);
    fetchJSON('/profiles/').then(data => {
      setProfiles(data);
      setLoading(false);
    });
  };

  useEffect(() => {
    refresh();
  }, []);

  return { profiles, loading, refresh };
}

export function useForumPosts() {
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);

  const refresh = () => {
    setLoading(true);
    fetchJSON('/forum/').then(data => {
      setPosts(data);
      setLoading(false);
    });
  };

  useEffect(() => {
    refresh();
  }, []);

  return { posts, loading, refresh };
}

export function createProfile(profileData) {
  return fetchJSON('/profiles/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(profileData),
  });
}

export function createPost(postData) {
  return fetchJSON('/forum/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(postData),
  });
}

export function reactToPost(postId, reaction) {
  return fetchJSON(`/forum/${postId}/react`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ reaction }),
  });
}

export function searchMatches(username) {
  return fetchJSON(`/matches/search?username=${encodeURIComponent(username)}`);
}

export function topMatches(username, n = 3) {
  return fetchJSON(`/matches/top?username=${encodeURIComponent(username)}&n=${n}`);
}
