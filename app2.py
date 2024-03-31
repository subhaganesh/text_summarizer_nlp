import streamlit as st
from textsummarizer.pipeline.prediction import PredictionPipeline

# Initialize the PredictionPipeline
obj = PredictionPipeline()

# Function to create a download link for text
def get_download_link(text, filename):
    href = f'<a href="data:text/plain;charset=utf-8,{text}" download="{filename}">Download Summarized Text</a>'
    return href

# Define the Streamlit app
def main():
    # Add CSS to set the background color of the entire app
    st.markdown(
        """
        <style>
        body {
            background-color: #f0f2f6; /* Light grey */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("Text Summarization")
    # Set background image
    st.markdown(
        """
        <style>
        .reportview-container {
            background: url("https://img.freepik.com/premium-photo/abstract-black-textured-background-with-scratches_130265-12474.jpg")
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Sidebar for user input
    st.sidebar.title("User Input")
    st.sidebar.write("Enter the text you want to summarize in the text box below.")
    text_input = st.sidebar.text_area("Input Text", height=400)  # Increase input box size

    # Separator
    st.sidebar.markdown("---")

    # Button to trigger summarization
    if st.sidebar.button("Summarize"):
        if text_input:
            try:
                # Perform summarization
                summary = obj.predict(text_input)
                st.subheader("Summary:")
                st.write(summary)

                # Download button for summarized conversation
                st.markdown(get_download_link(summary, filename="summary.txt"), unsafe_allow_html=True)

            except Exception as e:
                st.error("An error occurred during summarization.")
                st.error(e)
        else:
            st.warning("Please enter some text to summarize.")

    # About section
    st.sidebar.markdown("---")
    st.sidebar.subheader("About")
    st.sidebar.info(
        "This app uses a text summarization model to generate summaries of input text."
    )
    st.sidebar.info("Developed by Subhaganesh.")

# Run the app
if __name__ == "__main__":
    main()
