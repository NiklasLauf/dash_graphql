import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { GQLClient as RealComponent } from '../LazyLoader';

/**
 * ExampleComponent is an example component.
 * It takes a property, `label`, and
 * displays it.
 * It renders an input with the property `value`
 * which is editable by the user.
 */
export default class GQLClient extends Component {
    render() {
        return (
            <React.Suspense fallback={null}>
                <RealComponent {...this.props} />
            </React.Suspense>
        );
    }
}

GQLClient.defaultProps = {};

GQLClient.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,
    uri: PropTypes.string.isRequired,

    /**
     * A label that will be printed when this component is rendered.
     */
    query: PropTypes.string.isRequired,

    loading: PropTypes.bool,

    error: PropTypes.oneOfType([PropTypes.object, PropTypes.string]),

    /**
     * The value displayed in the input.
     */
    data: PropTypes.object,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};


export const defaultProps = GQLClient.defaultProps;
export const propTypes = GQLClient.propTypes;