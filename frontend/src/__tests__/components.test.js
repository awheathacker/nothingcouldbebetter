/**
 * Frontend component tests — nothingcouldbebetter.
 *
 * Tests the UI components module exports and API utilities.
 */

// Test: Navbar component exists
test('Navbar component is defined', () => {
  const { default: Navbar } = require('../components/Navbar');
  expect(typeof Navbar).toBe('function');
});

// Test: Footer component exists
test('Footer component is defined', () => {
  const { default: Footer } = require('../components/Footer');
  expect(typeof Footer).toBe('function');
});

// Test: ProfileCard component exists
test('ProfileCard component is defined', () => {
  const { default: ProfileCard } = require('../components/ProfileCard');
  expect(typeof ProfileCard).toBe('function');
});

// Test: MatchCard component exists
test('MatchCard component is defined', () => {
  const { default: MatchCard } = require('../components/MatchCard');
  expect(typeof MatchCard).toBe('function');
});

// Test: PostCard component exists
test('PostCard component is defined', () => {
  const { default: PostCard } = require('../components/PostCard');
  expect(typeof PostCard).toBe('function');
});

// Test: Page components exist
test('HomePage component exists', () => {
  const { default: HomePage } = require('../pages/HomePage');
  expect(typeof HomePage).toBe('function');
});

test('ProfilesPage component exists', () => {
  const { default: ProfilesPage } = require('../pages/ProfilesPage');
  expect(typeof ProfilesPage).toBe('function');
});

test('MatchesPage component exists', () => {
  const { default: MatchesPage } = require('../pages/MatchesPage');
  expect(typeof MatchesPage).toBe('function');
});

test('ForumPage component exists', () => {
  const { default: ForumPage } = require('../pages/ForumPage');
  expect(typeof ForumPage).toBe('function');
});

test('AboutPage component exists', () => {
  const { default: AboutPage } = require('../pages/AboutPage');
  expect(typeof AboutPage).toBe('function');
});

// Test: App component exists
test('App component is defined', () => {
  const App = require('../App.jsx');
  expect(typeof App.default).toBe('function');
});

// Test: API module exports
test('api module exports fetch utilities', () => {
  const api = require('../api');
  expect(typeof api.createProfile).toBe('function');
  expect(typeof api.createPost).toBe('function');
  expect(typeof api.searchMatches).toBe('function');
  expect(typeof api.useTaglines).toBe('function');
  expect(typeof api.useHero).toBe('function');
  expect(typeof api.useProfiles).toBe('function');
  expect(typeof api.useForumPosts).toBe('function');
});
