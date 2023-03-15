import React from 'react';

export default Author = (props) => {
    const { author } = props;
    return (
        <div>
            <div>
               { author.author_name } was born in {author.year_born}. 
            </div>
        </div>
    );
};