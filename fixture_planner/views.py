from django.shortcuts import render
from fixture_planner.models import AddPlTeamsToDB
from django.http import HttpResponse
from django.views import generic
from django.shortcuts import get_object_or_404
import fixture_planner.read_data as read_data


class FixturePlannerView(generic.ListView):
    model = AddPlTeamsToDB


def fill_data_base(request):
    df, names, short_names, ids = read_data.return_fixture_names_shortnames()
    print(df)
    number_of_teams = len(names)
    for i in range(number_of_teams):
        oppTeamNameList, oppTeamHomeAwayList, oppTeamDifficultyScore = [], [], []
        fill_model = AddPlTeamsToDB(team_name=names[i], team_id=ids[i], team_short_name=short_names[i])
        team_info = df.loc[i]
        for j in range(38):
            gw_info_TEAM_HA_SCORE = team_info.iloc[j + 1]
            oppTeamNameList.append(gw_info_TEAM_HA_SCORE[0])
            oppTeamHomeAwayList.append(gw_info_TEAM_HA_SCORE[1])
            oppTeamDifficultyScore.append(gw_info_TEAM_HA_SCORE[2])
        fill_model = AddPlTeamsToDB(team_name=names[i], team_id=ids[i], team_short_name=short_names[i],
                                    oppTeamDifficultyScore=oppTeamDifficultyScore,
                                    oppTeamHomeAwayList=oppTeamHomeAwayList,
                                    oppTeamNameList=oppTeamNameList)
        fill_model.save()

    return HttpResponse("Hello World2")


def index2(request):
    return HttpResponse("Hello World2")

class team_info:
    def __init__(self, opponent_team_name, difficulty_score, H_A, team_name):
        ...
        self.opponent_team_name = opponent_team_name
        self.difficulty_score = difficulty_score
        self.H_A = H_A
        self.team_name = team_name

def fixture_planner(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    fixture_list = AddPlTeamsToDB.objects.all()
    teams = len(fixture_list)
    gws = len(fixture_list[0].oppTeamNameList)
    gw_numbers = [i for i in range(38 - gws + 1, 38 + 1)]
    fixture_list = [fixture_list[i] for i in range(0, teams)]
    print(fixture_list)
    print(fixture_list[0])
    list = []
    for i in range(teams):
        temp_list = []
        team_i = fixture_list[i]
        for j in range(gws):
            temp_list.append(team_info(team_i.oppTeamNameList[j],
                                   team_i.oppTeamDifficultyScore[j],
                                   team_i.oppTeamHomeAwayList[j],
                                    team_i.team_name))
        list.append(temp_list)

    context = {
        'fixture_list': fixture_list,
        'teams': teams,
        'gws': gws,
        'gw_numbers': gw_numbers,
        'list': list,
    }

    # Render the HTML template index_catalog.html with the data in the context variable
    #return render(request, 'index_catalog.html', context=context)
    return render(request, 'fixture_planner_main.html', context=context)

