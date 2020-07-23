import React, { useState } from 'react';

type gridProps = {
	rows: number,
	cols: number
}

const Grid: React.FC<gridProps> = ({
	rows,
	cols
}) => {
	const [grid, setGrid] = useState(() => {
		let row = [];
		for (let i = 0; i < rows; i++) {
			row.push(Array.from(Array(cols), () => 0))
		}
		return row;
	});

	
	return (
		<div className="grid">
			{
			grid.map((rows, i) => rows.map(
				(col, j) => (
					<div 
						className="box"
						style={{
							backgroundColor: grid[i][j] ? 'black' : undefined
						}}
					/>
				)
			))
			}
		</div>
	)
}

export default Grid;