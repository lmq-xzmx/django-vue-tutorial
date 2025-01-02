const TOKEN_KEY = 'jwt_token';

export function getCurrentUser() {
  const token = localStorage.getItem(TOKEN_KEY);
  if (!token) return null;

  try {
    const payload = JSON.parse(atob(token.split('.')[1]));
    return { access: token, ...payload };
  } catch (e) {
    console.error('Invalid token:', e);
    return null;
  }
}

export function login(username, password) {
  return fetch('http://localhost:8000/api/token/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ username, password }),
  })
    .then(response => {
      if (!response.ok) {
        throw new Error('Login failed');
      }
      return response.json();
    })
    .then(data => {
      localStorage.setItem(TOKEN_KEY, data.access);
      return getCurrentUser();
    });
}

export function logout() {
  localStorage.removeItem(TOKEN_KEY);
}
