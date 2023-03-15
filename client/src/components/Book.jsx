import React from 'react';

const Book = (props) => {
    const { book } = props;
    console.log(book);
    return (
        <div>
            <div>
                {book.title} by {book.authorName.authorName} was released in {book.yearPublished} and has {book.review} stars.
            </div>
        </div>
    );
};

export default Book;