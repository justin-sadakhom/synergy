import React from 'react'
import ReactDom from 'react-dom'

ReactDom.render(<Home />, document.getElementById('root'))

function Home() {
    return(
        <div>
            <p>Hello</p>
        </div>
    )
}