interface Props {
  items: string[];
  heading: string;
}

function ListGroup({ items, heading }: Props) {
  return (
    <>
      <h1>{heading}</h1>
      <ul className="list-group">
        {items.map((item) => (
          <li className="list-group-item" key={item}>
            {item}
          </li>
        ))}
      </ul>
    </>
  );
}

export default ListGroup;