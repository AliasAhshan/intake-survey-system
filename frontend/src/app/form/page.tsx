'use client';
import { useEffect, useState } from 'react';

type Question = {
  id: string;
  text: string;
  type: string;
  options?: string[];
};

export default function FormPage() {
  const [form, setForm] = useState<{ title: string; questions: Question[] } | null>(null);

  useEffect(() => {
    fetch('http://localhost:5000/api/form')
      .then((res) => res.json())
      .then((data) => setForm(data))
      .catch((err) => console.error('Error fetching form:', err));
  }, []);

  return (
    <div className="p-6 max-w-xl mx-auto">
      <h1>{form?.title || 'Loading...'}</h1>
      <div>
        {form?.questions.map((q) => (
          <div key={q.id}>
            <p>{q.text}</p>
            {q.options?.map((opt) => (
              <label key={opt}>
                <input type="radio" name={q.id} value={opt} />
                {opt}
              </label>
            ))}
          </div>
        ))}
      </div>
    </div>
  );
}
