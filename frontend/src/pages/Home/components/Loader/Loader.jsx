import React from "react";
import "./Loader.css";

import MoonLoader from "react-spinners/MoonLoader";
import { css } from "@emotion/react";

function Loader({ loading }) {
const overrideCss = css`display: block;`;

    return (
    <div className="loader-container">
      <MoonLoader
        color="#E6483D"
        loading={loading}
        size={60}
        css={overrideCss}
      />
    </div>
  );
}
export default Loader;