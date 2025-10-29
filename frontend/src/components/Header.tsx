import ThemeToggle from "./ThemeToggle";

const Header: React.FC = () => {
  return (
    <header className="d-flex justify-content-around align-items-center">
      <div>BrickPredict</div>
      <ThemeToggle />
    </header>
  )
}

export default Header