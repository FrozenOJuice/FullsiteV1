"use client";

import { useEffect, useState } from "react";

interface Movie {
  id: number;
  title: string;
  year: number;
  rating: number;
}

export default function MoviesPage() {
  const [movies, setMovies] = useState<Movie[]>([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/movies")
      .then((res) => res.json())
      .then((data) => setMovies(data));
  }, []);

  return (
    <div>
      <h1>Movie List</h1>
      <ul>
        {movies.map((movie) => (
          <li key={movie.id}>
            {movie.title} ({movie.year}) - Rating: {movie.rating}
          </li>
        ))}
      </ul>
    </div>
  );
}
