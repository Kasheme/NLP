import dash

dash.register_page(__name__, order=3)

from dash import html, dcc
import dash_bootstrap_components as dbc

# ===== Create text objects
about_project_text = dcc.Markdown(
    """
    The purpose of this project was to identify the main topics in speeches by U.S. Presidents relating to conflict in the Middle East from the
    years 2003 (invasion of Iraq) to 2021 (final withdrawal of U.S. troops in Iraq). Included in the analysis are selected relevant speeches by
    U.S. Presidents: **George Bush** (6 speeches), **Barack Obama** (6 speeches), **Donald Trump** (3 speeches) and **Joe Biden** (3 speeches).

    If you are familiar with the U.S. invasion of Iraq in 2003, you will know that the initial justification for the invasion was to
    rid the then Iraq President Saddam Hussein of his supposed nuclear weapons arsenal. This was eventually disproven overtime, and as
    it became more difficult for the U.S. government to justify sustained military involvement in Iraq, the political discourse shifted
    to other reasons such as: democracy promotion, freedom and ensuring stability in the Middle East. 

    Simultaneously, a similar sentiment started to build surrounding the U.S. involvement in Afghanistan, especially after the killing
    of Al Qaeda leader Osama Bin Laden. 

    Therefore, I wanted to see if it was possible to prove or disprove this general sentiment by analysing as many speeches as possible
    relating to conflict in the Middle East using Natural Language Processing (NLP).

    To view the full code for the analysis and the dash application, please visit my [Github](https://github.com/Kasheme/NLP/tree/main/US%20Presedential%20Speeches).
    """
)

about_process_text = dcc.Markdown(
    """
    * Used Beautiful Soup to Web Scrape the speech transcripts for each U.S. President from a selection of websites.
    * Cleaned and Transformed each speech before combining the speeches into one document.
    * Tokenize the document into a list of sentences in the form of strings.
    * Ran a Top2Vec model using the new 'document' object as the input.
    * Tuned the hyper-parameters of the Top2Vec model to eventually return 25 topic buckets.
    * Where possible, used the top 50 words in each topic and top 20 documents (speech sentence) to manually attribute topic labels to each topic.
        - Top2Vec is an unsupervised machine learning technique and can not attribute topic labels automatically.
    * Calculate the [**Cosine Similarity Score**]("https://en.wikipedia.org/wiki/Cosine_similarity") between the topic bucket vectors and document vectors. Stored the results in a dataframe (2D table).
    """
)

about_topic_model_text = dcc.Markdown(
    """
    Top2Vec is an algorithm for topic modeling and semantic search. It automatically detects topics present in text and generates jointly embedded topic, document and word vectors.

    The assumption the algorithm makes is that many semantically similar documents are indicative of an underlying topic. The first step is to create a joint embedding of document and word vectors. 
    Once documents and words are embedded in a vector space the goal of the algorithm is to find dense clusters of documents, then identify which words attracted those documents together. 
    Each dense area is a topic and the words that attracted the documents to the dense area are the topic words.

    For more information on the Top2Vec method, including notebooks and tutorials, visit this [Github]("https://github.com/ddangelov/Top2Vec/blob/d70dab7079c050ef43b40327793283ea16967a27/README.md").
    """
)
# ===== Build card objects
about_project_card = dbc.Card(
    dbc.CardBody(
        [
            html.P(about_project_text)
        ],
        style={'width':'60rem'}
    )
)
about_process_card = dbc.Card(
    dbc.CardBody(
        [
            html.P(about_process_text)
        ],
        style={'width':'60rem'}
    )
)
about_topic_model_card = dbc.Card(
    dbc.CardBody(
        [
            html.P(about_topic_model_text)
        ],
        style={'width':'60rem'}
    )
)


# ===== Build tabs object
tabs = dbc.Tabs(
    [
        dbc.Tab(about_project_card, tab_id='tab_project', label='About the Project'),
        dbc.Tab(about_process_card, tab_id='tab_process', label='Process Review'),
        dbc.Tab(about_topic_model_card, tab_id='tab_tm', label='Topic Model Review')
    ],
    id='tabs',
    active_tab='tab_project',
    #className="pb-4",
    style={'width':'100%'}
    
)

layout = html.Div([
    html.Div(
        [
            dbc.Row(dbc.Col(html.Div("About", style={'font-size':22, 'textAlign': 'center'}) ) ),
            html.Hr() 
        ]
    ),
    dbc.Container(
        [
            dbc.Row(dbc.Col(tabs, className="bg-dark border"))
        ], style={'width':'80%', 'margin-left':'10rem'}, fluid=True
    )

])