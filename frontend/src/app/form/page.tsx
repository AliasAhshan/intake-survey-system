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
  const [answers, setAnswers] = useState<{ [key: string]: string }>({});

  useEffect(() => {
    fetch('http://localhost:5000/api/form')
      .then((res) => res.json())
      .then((data) => setForm(data))
      .catch((err) => console.error('Error fetching form:', err));
  }, []);

  const handleChange = (questionId: string, value: string) => {
    setAnswers((prev) => ({ ...prev, [questionId]: value }));
  };

  const handleSubmit = () => {
    fetch('http://localhost:5000/api/submit', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(answers),
    })
      .then((res) => res.json())
      .then((data) => {
        alert('Form submitted successfully!');
        console.log('Response:', data);
      })
      .catch((err) => {
        console.error('Error submitting form:', err);
        alert('Submission failed.');
      });
  };

  return (
    <div className="p-6 max-w-xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">{form?.title || 'Loading...'}</h1>
      <div>
        {form?.questions.map((q) => (
          <div key={q.id} className="mb-4">
            <p className="mb-2 font-semibold">{q.text}</p>
            {q.options?.map((opt) => (
              <label key={opt} className="mr-4">
                <input
                  type="radio"
                  name={q.id}
                  value={opt}
                  checked={answers[q.id] === opt}
                  onChange={() => handleChange(q.id, opt)}
                  className="mr-1"
                />
                {opt}
              </label>
            ))}
          </div>
        ))}
      </div>
      <button
        onClick={handleSubmit}
        className="mt-4 px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
      >
        Submit
      </button>
    </div>
  );
}
