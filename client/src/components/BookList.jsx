import React from 'react';
import Book from './Book';
import { useQuery, gql } from '@apollo/client';

const GET_ALL_BOOKS = gql`
query {
    allBooks {
      id
      title
      subtitle
      authorName {
        authorName
      }
      yearPublished
      review
    }
  }
`;

const BookList = () => {
    const { data } = useQuery(GET_ALL_BOOKS);
    
    return (
        <div>
            {data && (
                <>
                    {data.allBooks.map((book) => {
                        return <Book key={book.id} book={book} />
                    })}
                </>
            )}
        </div>
    );
};

export default BookList;